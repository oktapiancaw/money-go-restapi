from flask.globals import request

from flask_restful import fields, marshal


error_fields = {
  'url': fields.String(attribute='urlRequest'),
  'type': fields.String(attribute='typeRequest'),
  'status_code': fields.Integer(attribute='status_code'),
  'status': fields.String(attribute='statusRequest'),
  'message': fields.String(attribute='message'),
}

class ResultData():
  def returnApi(status_code, message ,data, statusRequest='success'):
    isEmpty = (data == '')
    if isEmpty:
      return {
        'status_code' : status_code,
        'statusRequest' : statusRequest,
        'message': message,
        'typeRequest': request.method,
        'urlRequest': request.url
      }
    else:
      return {
        'status_code' : status_code,
        'statusRequest' : statusRequest,
        'message': message,
        'typeRequest': request.method,
        'urlRequest': request.url,
        'data' : data
        }

  def returnMessage(status_code, message, statusRequest='success'):
    return marshal({
      'status_code' : status_code,
      'statusRequest' : statusRequest,
      'message': message,
      'typeRequest': request.method,
      'urlRequest': request.url
      }, error_fields)
      