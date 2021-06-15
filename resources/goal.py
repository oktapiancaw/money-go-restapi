from models.manage import ManageModel
from models.user import UserModel
from models.goal import GoalModel
from flask.globals import request
from templates.result import ResultData as resultTemplate
from flask_restful import Resource, marshal_with, reqparse, fields, marshal
from flask_httpauth import HTTPBasicAuth
from datetime import datetime
from app.app import db

auth = HTTPBasicAuth()

# Basic Validation for Request & Scaffold Request
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
  'url': fields.String(attribute='urlRequest'),
  'type': fields.String(attribute='typeRequest'),
  'status_code': fields.Integer(attribute='status_code'),
  'status': fields.String(attribute='statusRequest'),
  'message': fields.String(attribute='message'),
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
  def get(self):
    data = GoalModel.query.all()

    # Check if exist
    if not data:
      return resultTemplate.returnMessage(404, "No data in here", 'failed'), 404

    # Set currency
    for x in data:
      x.currency_now = ManageModel.getAllNominal(x.id)
      if x.currency_now == x.currency_target:
        x.status = 'finished'
    
    # Return data
    return marshal(resultTemplate.returnApi(200, 'All data has been loaded', data), return_fields), 200
  
  # [ Method : "POST" ] - Add a Data 
  @auth.login_required
  def post(self):
    parser.add_argument("title", help="Title of goals is required", required=True)
    parser.add_argument("end_date", help="End of goal", required=True)
    args = parser.parse_args()

    # Title Validation
    if args['title'] :
      if len(args['title']) >= 255 :
        return resultTemplate.returnMessage(400, 'Title is too long', 'failed'), 400
      if len(args['title']) <= 4 :
        return resultTemplate.returnMessage(400, 'Title is too short', 'failed'), 400

    # Tags Validation
    if args['tags'] :
      if len(args['tags']) >= 100 :
        return resultTemplate.returnMessage(400, 'Tags is too long', 'failed'), 400
      if len(args['tags']) <= 2 :
        return resultTemplate.returnMessage(400, 'Tags is too short', 'failed'), 400

    # End Date Validation
    if args['end_date']:
      if int(datetime.strptime(args['end_date'], '%Y-%m-%d').timestamp()) <= int(datetime.now().timestamp()):
        return resultTemplate.returnMessage(400, 'Cannot back to past month', 'failed'), 400

    # Currency Target Validation
    if args['currency_target'] :
      if int(args['currency_target']) <= 0:
        return resultTemplate.returnMessage(400, 'Currency target is too low', 'failed'), 400

      if int(args['currency_target']) >= 10000000000:
        return resultTemplate.returnMessage(400, 'Currency target is too high', 'failed'), 400

    # Save the request to database
    user_id = UserModel.query.filter_by(username=request.authorization.username).with_entities(UserModel.id)
    data = GoalModel(user_id=user_id, title=args['title'], tags=args['tags'], description=args['description'], start_date=args['start_date'], end_date=args['end_date'], currency_target=args['currency_target'])
    GoalModel.save(data)
    return marshal(resultTemplate.returnApi(201, 'Your data has been created!', data), return_fields), 201

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
    def get(self, id):
      data = GoalModel.query.filter_by(id=id).first()

      # Check if exist
      if not data:
        return resultTemplate.returnMessage(404, "Data isn't exist!", 'failed'), 404

      # Add currency now
      anu =  ManageModel.getAllNominal(id)
      data.currency_now = anu
      if data.currency_now == data.currency_target:
        data.status = 'finished'

      # Return the data
      return marshal(resultTemplate.returnApi(200, 'The data is founded', data), return_fields), 200

  # [ Method : "PATCH" ] - Update a Data 
    @auth.login_required
    def patch(self, id):
      parser.add_argument("title", help="Title of goals is required", required=False)
      parser.add_argument("end_date", help="End of goal", required=False)
      args = parser.parse_args()
      result = GoalModel.query.filter_by(id=id).first()

      # Filter if not the owner
      user_id = UserModel.query.filter_by(username=request.authorization.username).first().id
      if result.user_id != user_id:
        return resultTemplate.returnMessage(400, "This goal isn't your own", 'failed'), 400
      
      # If data is'nt exist
      if not result:
        return resultTemplate.returnMessage(404, "Data isn't exist!", 'failed'), 404

      # Title validation
      if args['title']:
        if len(args['title']) >= 255 :
          return resultTemplate.returnMessage(400, 'Title is too long', 'failed'), 400
        if len(args['title']) <= 4 :
          return resultTemplate.returnMessage(400, 'Title is too short', 'failed'), 400
        result.title = args['title']

      # Tags validation
      if args['tags']:
        if len(args['tags']) >= 100 :
          return resultTemplate.returnMessage(400, 'Tags is too long', 'failed'), 400
        if len(args['tags']) <= 2 :
          return resultTemplate.returnMessage(400, 'Tags is too short', 'failed'), 400
        result.tags = args['tags']

      # Insert description
      if args['description']:
        result.description = args['description']

      # Currency target validation
      if args['currency_target']:
        if int(args['currency_target']) <= 0:
          return resultTemplate.returnMessage(400, 'Currency target is too low', 'failed'), 400

        if int(args['currency_target']) >= 10000000000:
          return resultTemplate.returnMessage(400, 'Currency target is too high', 'failed'), 400
        result.currency_target = args['currency_target']

      # Update data
      GoalModel.update()
      return marshal(resultTemplate.returnApi(201, 'The data has been updated!', result), return_fields), 201

    @auth.login_required
    def delete(self, id):
      data = GoalModel.query.filter_by(id=id)

      # Check if exist
      if not data.first():
        return resultTemplate.returnMessage(404, "Data isn't exist!", 'failed'), 404
        
      # Delete
      data.delete()
      return resultTemplate.returnMessage(204, 'Data has been deleted!'), 204
