from models.user import UserModel
from models.manage import ManageModel
from models.goal import GoalModel
from flask.globals import request
from templates.result import ResultData as resultTemplate
from flask_restful import Resource, marshal_with, marshal, reqparse, fields
from flask_httpauth import HTTPBasicAuth
from datetime import datetime

auth = HTTPBasicAuth()

# Basic Validation for Request & Scaffold Request
parser = reqparse.RequestParser()
parser.add_argument('goal_id', help='Goal id is required', required=True)
parser.add_argument('nominal', type=int, help='How many you save money for the goals')
parser.add_argument('date', help='When u insert this management')
parser.add_argument('status', choices=('0','1','2'), help='Invalid status management')


# Return Template
resource_fields = {
  'id' : fields.Integer(attribute='id'),
  'goal_id': fields.Integer(attribute='goal_id'),
  'nominal': fields.Integer(attribute='nominal'),
  'date' : fields.DateTime(attribute='date'),
  'status' : fields.Integer(attribute='status')
}

return_fields = {
  'url': fields.String(attribute='urlRequest'),
  'type': fields.String(attribute='typeRequest'),
  'status_code': fields.Integer(attribute='status_code'),
  'status': fields.String(attribute='statusRequest'),
  'message': fields.String(attribute='message'),
  'data': fields.Nested(resource_fields)
}

class ManageList(Resource, resultTemplate):

  # Authentication
  @auth.verify_password
  def verify_password(username, password):
    user = UserModel.query.filter_by(username = username).first()
    if not user or not user.verify_password(password):
      return False
    user.User = user
    return True
  

  # [ Method : "GET" ] - Get all Data 
  @auth.login_required
  def get(self):
    data = ManageModel.query.all()

    # Check if exist
    if not data:
      return resultTemplate.returnMessage(404, "Data isn't exist!", 'failed'), 404
    
    # Return data
    return marshal(resultTemplate.returnApi(200, 'All data has been loaded', data), return_fields), 200


  # [ Method : "POST" ] - Add a Data 
  @auth.login_required
  def post(self):
    args = parser.parse_args()
    goal = GoalModel.query.filter_by(id=args['goal_id']).first()
    
    # Check Goal if exist
    if not goal:
      return resultTemplate.returnMessage(404, "Data isn't exist!", 'failed'), 404
    
    # Get Total currency now
    total_currency = ManageModel.getAllNominal(goal.id)

    # Currency validation
    if total_currency >= goal.currency_target:
      if args['status'] == '1':
        return resultTemplate.returnMessage(400, 'youre already finish this goal', 'failed'), 400

    # If already create today
    alreadyManage = ManageModel.query.filter_by(date=args['date'], goal_id=args['goal_id']).first()
    if alreadyManage:
      return resultTemplate.returnMessage(400, 'You already add data today', 'failed'), 400

    # Date validation
    if args['date']:
      if datetime.strptime(args['date'], '%Y-%m-%d').month > 12 and datetime.strptime(args['date'], '%Y-%m-%d').month < 1:
        return resultTemplate.returnMessage(400, 'Invalid month', 'failed'), 400

      if datetime.strptime(args['date'], '%Y-%m-%d').day > 31 and datetime.strptime(args['date'], '%Y-%m-%d').day < 1:
        return resultTemplate.returnMessage(400, 'Invalid date', 'failed'), 400

    # Nominal validation
    if args['nominal']:
      if int(args['nominal']) < 0:
        return resultTemplate.returnMessage(400, 'Nominal is too low', 'failed'), 400

      if int(args['nominal']) >= total_currency or int(args['nominal']) >= 10000000000:
        return resultTemplate.returnMessage(400, 'Nominal is too high', 'failed'), 400

    # Save the request to database
    data = ManageModel(goal_id=args['goal_id'], nominal=args['nominal'],date=args['date'], status=args['status'])
    ManageModel.save(data)
    return marshal(resultTemplate.returnApi(201, 'Manage has been created', data), return_fields), 201

class ManageData(Resource, resultTemplate):

  #Authentication
  @auth.verify_password
  def verify_password(username, password):
    user = UserModel.query.filter_by(username = username).first()
    if not user or not user.verify_password(password):
      return False
    user.User = user
    return True


  # [ Method : "GET" ] - Get data by id
  @auth.login_required
  def get(self, id):
    data = ManageModel.query.filter_by(id=id).first()

    # Check if exist
    if not data:
      return resultTemplate.returnMessage(404, "Data isn't exist!", 'failed'), 404
    
    # Return the data
    return marshal(resultTemplate.returnApi(200, 'The data is founded', data), return_fields), 200


  # [ Method : "DELETE" ] - Delete a Data 
  @auth.login_required
  def delete(self, id):
    data = ManageModel.query.filter_by(id=id)

    # Check if exist
    if not data.first():
      return resultTemplate.returnMessage(404, "Data isn't exist!", 'failed'), 404

    # Delete
    data.delete()
    return resultTemplate.returnMessage(200, 'Data has been deleted!'), 204