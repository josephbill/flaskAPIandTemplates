from .dbconfig import db 

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content  = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref='posts')

    def __repr__(self) -> str:
        return f"Post {self.content}"


# what does the Lazy attribute help with.