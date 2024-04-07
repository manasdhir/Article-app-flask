from flask import Flask
from flask_restful import Api
from application.database import db

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db.init_app(app)
api=Api(app)
app.app_context().push()

from application.controllers import *

from application.api import UserAPI

api.add_resource(UserAPI,"/api/user","/api/user/<string:username>")
 
if __name__=="__main__":
    app.run(debug=True,port=8000)



