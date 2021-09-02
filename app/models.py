from app import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True, unique=True)
    post = db.Column(db.String(120), index=True)

    def __repr__(self):
        return(f"<User>: {self.username}, <Post>: {self.post}")