from models.user import UserModel
from flask_restful import Resource, abort, marshal, reqparse, fields

resource_fields = {
    'id' : fields.Integer,
    'username' : fields.String
}
return_fields = {
  'url': fields.String(attribute='urlRequest'),
  'type': fields.String(attribute='typeRequest'),
  'status_code': fields.Integer(attribute='status_code'),
  'status': fields.String(attribute='statusRequest'),
  'message': fields.String(attribute='message'),
  'data': fields.Nested(resource_fields)
}
parser = reqparse.RequestParser()

class User(Resource, resultTemplate):
    def post(self):
        parser.add_argument("username", help="Username is Required", required=True)
        parser.add_argument("password", help="Password is Required", required=True)
        args = parser.parse_args()
        if UserModel.query.filter_by(username=args['username']).first() is not None:
            return resultTemplate.returnMessage(400, 'Username already used', 'failed'), 201
            
        user = UserModel(username=args['username'])
        user.hash_password(args['password'])
        UserModel.save(user)

        return resultTemplate.returnApi(201, 'User has been created', user), 201

