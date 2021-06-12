from flask.globals import request

class ResultData():
  def returnApi(statusUrl, message ,data):
      isEmpty = (data == '')
      if isEmpty:
        return {
          'status' : statusUrl,
          'typeRequest': request.method,
          'urlRequest': request.url,
          'message': message
        }
      else:
        return {
          'status' : statusUrl,
          'typeRequest': request.method,
          'urlRequest': request.url,
          'message': message,
          'data' : data
          }