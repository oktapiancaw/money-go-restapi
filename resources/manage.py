from resources import user
from models.user import UserModel
from flask.globals import request
from models.manage import ManageModel
from templates.result import ResultData
from flask_restful import Resource, abort, marshal_with, reqparse, fields
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

parser = reqparse.RequestParser()
resource_fields = {
  'id' : fields.Integer(attribute='id'),
  'title' : fields.String(attribute='title'),
  'date' : fields.DateTime(attribute='date'),
  'status' : fields.Integer(attribute='status')
}

return_fields = {
  'status': fields.Integer(attribute='status'),
  'type': fields.String(attribute='typeRequest'),
  'url': fields.String(attribute='urlRequest'),
  'data': fields.Nested(resource_fields)
}

class ManageList(Resource, ResultData):
  
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
    return ResultData.returnApi(200, 'All data has been loaded', data), 200