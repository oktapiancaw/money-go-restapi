from sqlalchemy import ForeignKey
from app.app import db

class ManageModel(db.Model):
  __tablename__ = 'manage'

  id = db.Column(db.Integer, primary_key=True)
  goal_id = db.Column(db.Integer, ForeignKey('goals.id'))
  title = db.Column(db.String(255))
  nominal = db.Column(db.BigInteger)
  date = db.Column(db.DateTime)
  status = db.Column(db.Integer)

  def save(data):
    db.session.add(data)
    db.session.commit()

  def update():
    db.session.commit()

  def __repr__(self):
    return f"Manage(title = {self.title}, nominal = {self.nominal}, date = {self.date}, status = {self.status})"