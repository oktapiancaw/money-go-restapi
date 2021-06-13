from models.manage import ManageModel
from models.user import UserModel
from models.goal import GoalModel
from flask.globals import request
from templates.result import ResultData as resultTemplate
from flask_restful import Resource, abort, marshal_with, reqparse, fields
from flask_httpauth import HTTPBasicAuth
from datetime import datetime
from app.app import db

auth = HTTPBasicAuth()

# Basic Validation for Request
parser = reqparse.RequestParser()
parser.add_argument("tags", help="Tags of goal")
parser.add_argument("start_date", help="Start of goal")
parser.add_argument("description", help="Description of goals")
parser.add_argument("currency_target", type=int, help="Currency target of goals")

# Return Template
resource_fields = {
  'id' : fields.Integer(attribute='id'),
  'title' : fields.String(attribute='title'),
  'tags' : fields.String(attribute='tags'),
  'start_date' : fields.DateTime(attribute='start_date'),
  'end_date' : fields.DateTime(attribute='end_date'),
  'description' : fields.String(attribute='description'),
  'currency_target' : fields.Integer(attribute='currency_target'),
  'currency_now' : fields.Integer(attribute='currency_now'),
  'status' : fields.String(attribute='status', default='unfinished')
}
return_fields = {
  'status': fields.Integer(attribute='status'),
  'type': fields.String(attribute='typeRequest'),
  'url': fields.String(attribute='urlRequest'),
  'data': fields.Nested(resource_fields)
}


class GoalList(Resource, resultTemplate):

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
  @marshal_with(return_fields)
  def get(self):
    data = GoalModel.query.all()
    if not data:
      abort(404, method="GET", message="No data here")
    for x in data:
      x.currency_now = ManageModel.getAllNominal(x.id)
      if x.currency_now == x.currency_target:
        x.status = 'finished'
    
    return resultTemplate.returnApi(200, 'All data has been loaded', data)
  
  # [ Method : "POST" ] - Add a Data 
  @auth.login_required
  @marshal_with(return_fields)
  def post(self):
    parser.add_argument("title", help="Title of goals is required", required=True)
    parser.add_argument("end_date", help="End of goal", required=True)
    args = parser.parse_args()

    # Title Validation
    if args['title'] :
      if len(args['title']) >= 255 :
        abort(400, message="currency target is too long")
      if len(args['title']) <= 4 :
        abort(400, message="title is too short")

    # Tags Validation
    if args['tags'] :
      if len(args['tags']) >= 100 :
        abort(400, message="currency target is too long")
      if len(args['tags']) <= 2 :
        abort(400, message="tags is too short")

    # End Date Validation
    if args['end_date']:
      if int(datetime.strptime(args['end_date'], '%Y-%m-%d').timestamp()) <= int(datetime.now().timestamp()):
        abort(400, message="Cant back to past!")

    # Currency Target Validation
    if args['currency_target'] :
      if int(args['currency_target']) <= 0:
        abort(400, "currency target is too low")

      if int(args['currency_target']) >= 10000000000:
        abort(400, "currency target is too high")

    # Save the request to database
    user_id = UserModel.query.filter_by(username=request.authorization.username).with_entities(UserModel.id)
    data = GoalModel(user_id=user_id, title=args['title'], tags=args['tags'], description=args['description'], start_date=args['start_date'], end_date=args['end_date'], currency_target=args['currency_target'])
    GoalModel.save(data)
    return resultTemplate.returnApi(201, 'Your data has been created!', data), 201

class Goal(Resource, resultTemplate):
    # Authentication
    @auth.verify_password
    def verify_password(username, password):
      user = UserModel.query.filter_by(username = username).first()
      if not user or not user.verify_password(password):
        return False
      user.User = user
      return True

  # [ Method : "GET" ] - Get a Data 
    @auth.login_required
    @marshal_with(return_fields)
    def get(self, id):
      # Filter data
      data = GoalModel.query.filter_by(id=id).first()
      if not data:
        abort (404, method="GET", message="Data isn't exists")

      # Add currency now
      anu =  ManageModel.getAllNominal(id)
      data.currency_now = anu
      if data.currency_now == data.currency_target:
        data.status = 'finished'
      # Return the data
      return resultTemplate.returnApi(200, 'The data is founded', data), 200

  # [ Method : "PATCH" ] - Update a Data 
    @auth.login_required
    @marshal_with(return_fields)
    def patch(self, id):
      parser.add_argument("title", help="Title of goals is required")
      parser.add_argument("end_date", help="End of goal")
      args = parser.parse_args()
      result = GoalModel.query.filter_by(id=id).first()

      # Filter if not the owner
      user_id = UserModel.query.filter_by(username=request.authorization.username).with_entities(UserModel.id)
      if result.user_id != user_id:
        abort(400, message="Goal isn't yours")
      
      # If data is'nt exist
      if not result:
        abort(400, message="Goal isn't exists, cant update")

      # Title validation
      if args['title']:
        if len(args['title']) >= 255 :
          abort(400, message="title is too long")
        if len(args['title']) <= 4 :
          abort(400, message="title is too short")
        result.title = args['title']

      # Tags validation
      if args['tags']:
        if len(args['tags']) >= 100 :
          abort(400, message="tags is too long")
        if len(args['tags']) <= 2 :
          abort(400, message="tags is too short")
        result.tags = args['tags']

      # Insert description
      if args['description']:
        result.description = args['description']

      # Currency target validation
      if args['currency_target']:
        if int(args['currency_target']) <= 0:
            abort(400, "currency target is too low")

        if int(args['currency_target']) >= 10000000000:
          abort(400, "currency target is too high")
        result.currency_target = args['currency_target']

      # Update data
      GoalModel.update()
      return resultTemplate.returnApi(201, 'The data has been updated!', result), 201

    @auth.login_required
    def delete(self, id):
      # Filter data
      data = GoalModel.query.filter_by(id=id)
      if not data.first():
        abort(404, message="data isn't exist!")
        
      # Delete
      data.delete()
      return resultTemplate.returnApi(200, 'Data has been deleted!', ''), 204
