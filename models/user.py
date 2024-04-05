from .dbconfig import db 

class User(db.Model):
    # columns 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)

    # constructors and various helper methods for the record/object instance 

    def __repr__(self) -> str:
        return f"User {self.username}"