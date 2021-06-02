from flask_migrate import Migrate
from flask_restful import Api, request
from resources.goal import Goal, GoalList
from resources.user import User
from models.goal import GoalModel
from models.user import UserModel
from app.app import create_app, db
from werkzeug.security import check_password_hash
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

app = create_app()
migrate = Migrate(app, db)



# API
api = Api(app)
api.add_resource(GoalList, "/")
api.add_resource(User, "/users")
api.add_resource(Goal, "/<int:id>")
if __name__ == '__main__':
    app.run(port=6000)