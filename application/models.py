from application.database import db

class user(db.Model):
    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
class Article(db.Model):
    article_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    authors = db.relationship("user", secondary="article_authors")
class ArticleAuthors(db.Model):
    user_id = db.Column(db.Integer,   db.ForeignKey("user.user_id"), primary_key=True, nullable=False)
    article_id = db.Column(db.Integer,  db.ForeignKey("article.article_id"), primary_key=True, nullable=False)

