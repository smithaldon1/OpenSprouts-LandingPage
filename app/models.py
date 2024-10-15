from . import db
from datetime import datetime as dt

# Waitlist Model
class Waitlist(db.Model):
    """ Data model for website waitlist """
    __tablename__ = "waitlist"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    created = db.Column(db.DateTime, index=False, unique=False, nullable=False)
    email = db.Column(db.String(255), index=False, unique=True, nullable=False)

    def __init__(self, email):
        self.email = email
        self.created = dt.now()

    def __repr__(self):
        return f"Waitlist(id={self.id!r}, created={self.created}, email={self.email})"