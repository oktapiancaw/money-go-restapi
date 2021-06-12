from resources import user
from models.user import UserModel
from flask.globals import request
from models.goal import GoalModel
from templates.result import ResultData
from flask_restful import Resource, abort, marshal_with, reqparse, fields
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

parser = reqparse.RequestParser()
resource_fields = {
    'id' : fields.Integer(attribute='id'),
    'title' : fields.String(attribute='title'),
    'tags' : fields.String(attribute='tags'),
    'start_date' : fields.DateTime(attribute='start_date'),
    'end_date' : fields.DateTime(attribute='end_date'),
    'description' : fields.String(attribute='description'),
    'currency_target' : fields.Integer(attribute='currency_target')
}
return_fields = {
    'status': fields.Integer(attribute='status'),
    'type': fields.String(attribute='typeRequest'),
    'url': fields.String(attribute='urlRequest'),
    'data': fields.Nested(resource_fields)
}


class GoalList(Resource, ResultData):
    
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
        data = GoalModel.query.all()
        if not data:
            abort(404, method="GET", message="No data here")
        return ResultData.returnApi(200, 'All data has been loaded', data), 200
    
    @auth.login_required
    @marshal_with(return_fields)
    def post(self):
        # parser.add_argument("id", help="id of goals is required", required=True)
        parser.add_argument("title", help="Title of goals is required", required=True)
        parser.add_argument("tags", help="Tags of goal")
        parser.add_argument("start_date", help="Start of goal")
        parser.add_argument("end_date", help="End of goal", required=True)
        parser.add_argument("description", help="Description of goals")
        parser.add_argument("currency_target", help="Currency target of goals")
        args = parser.parse_args()
        if args['title'] :
            if len(args['title']) >= 255 :
                abort(400, message="currency target is to long")

        if args['tags'] :
            if len(args['tags']) >= 200 :
                abort(400, message="currency target is to long")

        if args['currency_target'] :
            if args['currency_target'] >= 2147483647 :
                abort(400, message="currency target is to much")

            if args['currency_target'] <= -2147483647 :
                abort(400, message="currency target is to bits")
        
        data = GoalModel(title=args['title'], tags=args['tags'], description=args['description'], start_date=args['start_date'], endDate=args['endDate'], currency_target=args['currency_target'])
        GoalModel.save(data)
        return ResultData.returnApi(201, 'Your data has been created!', data), 201

class Goal(Resource, ResultData):
    @auth.verify_password
    def verify_password(username, password):
        user = UserModel.query.filter_by(username = username).first()
        if not user or not user.verify_password(password):
            return False
        user.User = user
        return True

    @auth.login_required
    @marshal_with(return_fields)
    def get(self, id):
        result = GoalModel.query.filter_by(id=id).first()
        if not result:
            abort (404, method="GET", message="Data isn't exists")
        return ResultData.returnApi(200, 'The data is founded', result), 200

    @auth.login_required
    @marshal_with(return_fields)
    def patch(self, id):
        parser.add_argument("title", help="Title of goals")
        parser.add_argument("tags", help="Tags of goal")
        parser.add_argument("end_date", help="End of goal")
        parser.add_argument("description", help="Description of goals")
        parser.add_argument("currency_target", help="Currency target of goals")
        args = parser.parse_args()
        result = GoalModel.query.filter_by(id=id).first()
        if not result:
            abort(400, message="Goal isn't exists, cant update")

        if args['title']:
            if len(args['title']) >= 255 :
                abort(400, message="currency target is to long")
            result.title = args['title']

        if args['tags']:
            result.tags = args['tags']
            if len(args['tags']) >= 200 :
                abort(400, message="currency target is to long")

        if args['description']:
            result.description = args['description']

        if args['currency_target']:
            result.currency_target = args['currency_target']
            if args['currency_target'] >= 2147483647 :
                abort(400, message="currency target is to much")

            if args['currency_target'] <= -2147483647 :
                abort(400, message="currency target is to bits")

        GoalModel.update()

        return ResultData.returnApi(201, 'The data has been updated!', result), 201

    @auth.login_required
    def delete(self, id):
        GoalModel.query.filter_by(id=id).delete()
        return ResultData.returnApi(200, 'Data has been deleted!', ''), 204