
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# import datetime

class GoalModel(db.Model):
    __tablename__ = 'goals'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    type = db.Column(db.String(100))
    description = db.Column(db.String)
    currency_target = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def save(data):
        db.session.add(data)
        db.session.commit()

    def update():
        db.session.commit()
        
    def __repr__(self):
        return f"Goal(title = { self.title }, type = { self.type }, description = { self.description }, currency_target = { self.currency_target }, created_at = { self.created_at }, updated_at = { self.updated_at })"
