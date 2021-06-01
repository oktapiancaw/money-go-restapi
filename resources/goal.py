
from models.goal import GoalModel
from flask_restful import Resource, abort, marshal_with, reqparse, fields

parser = reqparse.RequestParser()
resoruce_fields = {
    'id' : fields.Integer,
    'title' : fields.String,
    'type' : fields.String,
    'description' : fields.String,
    'currency_target' : fields.Integer
}



class Goal(Resource):
    @marshal_with(resoruce_fields)
    def get(self):
        result = GoalModel.query.all()
        if not result:
            abort(404, method="GET", message="No data here")
        return result

    @marshal_with(resoruce_fields)
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