
from resources import user
from models.user import UserModel
from flask.globals import request
from models.goal import GoalModel
from flask_restful import Resource, abort, marshal_with, reqparse, fields
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

parser = reqparse.RequestParser()
resource_fields = {
    'id' : fields.Integer,
    'title' : fields.String,
    'type' : fields.String,
    'description' : fields.String,
    'currency_target' : fields.Integer
}



class GoalList(Resource):
    @auth.verify_password
    def verify_password(username, password):
        user = UserModel.query.filter_by(username = username).first()
        if not user or not user.verify_password(password):
            return False
        user.User = user
        return True

    @auth.login_required
    @marshal_with(resource_fields)
    def get(self):
        result = GoalModel.query.all()
        if not result:
            abort(404, method="GET", message="No data here")
        return result
    
    @auth.login_required
    @marshal_with(resource_fields)
    def post(self):
        # parser.add_argument("id", help="id of goals is required", required=True)
        parser.add_argument("title", help="Title of goals is required", required=True)
        parser.add_argument("type", help="Type of goals")
        parser.add_argument("description", help="Description of goals")
        parser.add_argument("currency_target", help="Currency target of goals")
        args = parser.parse_args()
        result = GoalModel(title=args['title'], type=args['type'], description=args['description'], currency_target=args['currency_target'])
        GoalModel.save(result)
        return result, 201

class Goal(Resource):
    @auth.verify_password
    def verify_password(username, password):
        user = UserModel.query.filter_by(username = username).first()
        if not user or not user.verify_password(password):
            return False
        user.User = user
        return True

    @auth.login_required
    @marshal_with(resource_fields)
    def get(self, id):
        result = GoalModel.query.filter_by(id=id).first()
        if not result:
            abort (404, method="GET", message="Data isn't exists")
        return result

    @auth.login_required
    @marshal_with(resource_fields)
    def patch(self, id):
        parser.add_argument("title", help="Title of goals")
        parser.add_argument("type", help="Type of goals")
        parser.add_argument("description", help="Description of goals")
        parser.add_argument("currency_target", help="Currency target of goals")
        args = parser.parse_args()
        result = GoalModel.query.filter_by(id=id).first()
        if not result:
            abort(409, message="Goal isn't exists, cant update")

        if args['title']:
            result.title = args['title']
        if args['type']:
            result.type = args['type']
        if args['description']:
            result.description = args['description']
        if args['currency_target']:
            result.currency_target = args['currency_target']

        GoalModel.update()

        return result

    @auth.login_required
    def delete(self, id):
        GoalModel.query.filter_by(id=id).delete()
        return {"text" : "success"}, 204