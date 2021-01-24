from app import db
from datetime import datetime

class Card(db.Model):
    """ Card Model """

    __tablename__ = 'card'

    id = db.Column(db.Integer, primary_key=True)
    creditcardnumber = db.Column(db.Integer)
    cardholder = db.Column(db.String(20), nullable=False)
    expirationdate = db.Column(db.Integer)
    securitycode = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, name):
        self.cardholder = name


    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Card.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __str__(self):
        return "Card: {}".format(self.cardholder)