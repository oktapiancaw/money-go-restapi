from sqlalchemy import ForeignKey
from app.app import db

class ManageModel(db.Model):
  __tablename__ = 'manage'

  id = db.Column(db.Integer, primary_key=True)
  goal_id = db.Column(db.Integer, ForeignKey('goals.id'))
  nominal = db.Column(db.BigInteger, default=0)
  date = db.Column(db.DateTime)
  status = db.Column(db.Integer, default=0)

  def save(data):
    db.session.add(data)
    db.session.commit()

  def update():
    db.session.commit()

  def __repr__(self):
    return f"Manage(nominal = {self.nominal}, date = {self.date}, status = {self.status})"