from app import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)