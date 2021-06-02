from models.user import UserModel
from flask_restful import Resource, abort, marshal_with, reqparse, fields

resource_fields = {
    'id' : fields.Integer,
    'username' : fields.String
}
parser = reqparse.RequestParser()

class User(Resource):
    @marshal_with(resource_fields)
    def post(self):
        parser.add_argument("username", help="Username is Required", required=True)
        parser.add_argument("password", help="Password is Required", required=True)
        args = parser.parse_args()
        if UserModel.query.filter_by(username=args['username']).first() is not None:
            abort(400, message='Username already used')
        user = UserModel(username=args['username'])
        user.hash_password(args['password'])
        UserModel.save(user)

        return user, 201

