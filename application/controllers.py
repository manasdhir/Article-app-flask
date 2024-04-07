from flask import Flask, request
from flask import render_template
from flask import current_app as app
from application.models import Article

@app.route('/',methods=['GET','POST'])
def home():
    articles=Article.query.all()
    print(articles)
    return render_template("home.html",articles=articles)

@app.route('/articles_by/<user_name>',methods=['GET','POST'])
def articles_by_author(user_name):
    articlus=Article.query.filter(Article.authors.any(username=user_name)).all()
    print(articlus)
    return render_template("artbyauthor.html",articles=articlus,username=user_name)