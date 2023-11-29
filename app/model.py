from . import db

class Flight(db.Model):
    __tablename__ = "flights"
    id = db.Column(db.Integer, primary_key = True)
    duration = db.Column(db.DateTime, nullable=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100),unique=True)
    m_id = db.relationship(Flight,backref="flight_ticket",lazy='dynamic')

    def __init__(self, email, **kwargs):
        super(User, self).__init__(**kwargs)
        self.email = email

    def check_month_remaining(self):
        a = Flight.query.filter_by(flight_ticket= self).all()
        return a