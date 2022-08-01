from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class EmployeeModel(db.Model):
    __tablename__ = "table"

    name = db.Column(db.String())
    place = db.Column(db.String())
    email = db.Column(db.String(), primary_key=True)



    def __init__(self,  name, place, email):
        self.name = name
        self.place = place
        self.email = email

    def __repr__(self):
        return f"{self.name}:{self.email}"