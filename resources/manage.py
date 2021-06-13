from models.user import UserModel
from flask.globals import request
from models.manage import ManageModel
from models.goal import GoalModel
from templates.result import ResultData as resultTemplate
from flask_restful import Resource, abort, marshal_with, reqparse, fields
from flask_httpauth import HTTPBasicAuth
from datetime import datetime
auth = HTTPBasicAuth()

parser = reqparse.RequestParser()
resource_fields = {
  'id' : fields.Integer(attribute='id'),
  'goal_id': fields.Integer(attribute='goal_id'),
  'nominal': fields.Integer(attribute='nominal'),
  'date' : fields.DateTime(attribute='date'),
  'status' : fields.Integer(attribute='status')
}

return_fields = {
  'status': fields.Integer(attribute='status'),
  'type': fields.String(attribute='typeRequest'),
  'url': fields.String(attribute='urlRequest'),
  'data': fields.Nested(resource_fields)
}


class ManageList(Resource, resultTemplate):
  @auth.verify_password
  def verify_password(username, password):
    user = UserModel.query.filter_by(username = username).first()
    if not user or not user.verify_password(password):
      return False
    user.User = user
    return True
  
  @auth.login_required
  @marshal_with(return_fields)
  def get(self):
    data = ManageModel.query.all()
    if not data:
      abort(404, method="GET", message="No data here")
    return resultTemplate.returnApi(200, 'All data has been loaded', data), 200

  @auth.login_required
  # @marshal_with(return_fields)
  def post(self):
    parser.add_argument('goal_id', help='Goal id is required', required=True)
    parser.add_argument('nominal', type=int, help='How many you save money for the goals')
    parser.add_argument('date', help='When u insert this management')
    parser.add_argument('status', choices=('0','1','2'), help='Invalid status management')
    args = parser.parse_args()
    goal = GoalModel.query.filter_by(id=args['goal_id']).first()
    total_currency = ManageModel.getAllNominal(goal.id)
    if total_currency >= goal.currency_target:
      if args['status'] == '1':
        abort(404, message="your goal is finished")
      
    if not goal:
      abort(404, message="Goal isn't exist!")

    alreadyManage = ManageModel.query.filter_by(date=args['date'], goal_id=args['goal_id']).first()
    if alreadyManage:
      abort(400, message="You already add data today")

    if args['date']:
      if datetime.strptime(args['date'], '%Y-%m-%d').month > 12 and datetime.strptime(args['date'], '%Y-%m-%d').month < 1:
        abort(400, message="Invalid Month")

      if datetime.strptime(args['date'], '%Y-%m-%d').day > 31 and datetime.strptime(args['date'], '%Y-%m-%d').day < 1:
        abort(400, message="Invalid Day")

    if args['nominal']:
      if int(args['nominal']) < 0:
        abort(400, message="nominal is too low")

      if int(args['nominal']) >= 10000000000:
        abort(400, message="nominal is too high")

    data = ManageModel(goal_id=args['goal_id'], nominal=args['nominal'],date=args['date'], status=args['status'])
    ManageModel.save(data)
    return resultTemplate.returnApi(201, 'Manage has been created', data), 201

class Manage(Resource, resultTemplate):
  @auth.verify_password
  def verify_password(username, password):
    user = UserModel.query.filter_by(username = username).first()
    if not user or not user.verify_password(password):
      return False
    user.User = user
    return True

  def get(self, id):
    data = ManageModel.query.filter_by(id=id).first()
    if not data:
      abort (404, method="GET", message="Data isn't exists")
    return resultTemplate.returnApi(200, 'The data is founded', data), 200

  def delete(self, id):
    data = ManageModel.query.filter_by(id=id)
    if not data.first():
      abort (404, method="GET", message="Data isn't exists")

    data.delete()
    return resultTemplate.returnApi(200, 'Data has been deleted!', ''), 204