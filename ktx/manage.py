from app import db
from models import User

if __name__ == '__main__':
    db.create_all()