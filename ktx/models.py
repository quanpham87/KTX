from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    username = db.Column(db.String(25))
    password = db.Column(db.String(50))
    date_joined = db.Column(db.DateTime)
    date_last_logged_in = db.Column(db.DateTime)

    def __init__(self, first_name, last_name, username, password, date_joined=None, date_last_logged_in=None):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        if date_joined is None:
            date_joined = datetime.utcnow()
        if date_last_logged_in is None:
            date_last_logged_in = datetime.utcnow()
        self.date_joined = date_joined
        self.date_last_logged_in = date_last_logged_in