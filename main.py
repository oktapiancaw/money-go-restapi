from flask_migrate import Migrate
from flask_restful import Api
from resources.goal import Goal, GoalList
from models.goal import GoalModel, db
from app import create_app

app = create_app()
migrate = Migrate(app, db)
# API

api = Api(app)
api.add_resource(GoalList, "/")
api.add_resource(Goal, "/<int:id>")

if __name__ == '__main__':
    app.run(port=6000)