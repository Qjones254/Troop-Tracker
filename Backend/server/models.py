from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData



metadata = MetaData()

db = SQLAlchemy(metadata=metadata)


class Personnel(db.Model):
    __tablename__ = 'personnels'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True )
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    rank = db.Column(db.String(30), nullable=False)
    phone_number= db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    joining_date = db.Column(db.DateTime, nullable=False)
    last_update = db.Column(db.DateTime, nullable=False)
    

def __repr__(self):
        return f'<Personnel {self.first_name} {self.last_name}>' 


