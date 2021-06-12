from sqlalchemy import ForeignKey
from app.app import db
# import datetime

class GoalModel(db.Model):
    __tablename__ = 'goals'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('users.id'))
    title = db.Column(db.String(255))
    tags = db.Column(db.String(100))
    description = db.Column(db.String)
    currency_target = db.Column(db.BigInteger)
    start_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    end_date = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def save(data):
        db.session.add(data)
        db.session.commit()

    def update():
        db.session.commit()

    def __repr__(self):
        return f"Goal(title = { self.title }, tags = { self.tags }, description = { self.description }, currency_target = { self.currency_target }, start_date = { self.start_date }, end_date = { self.end_date }, created_at = { self.created_at }, updated_at = { self.updated_at })"
