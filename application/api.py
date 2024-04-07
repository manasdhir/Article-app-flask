from flask_restful import Resource,fields,marshal_with
from application.models import user,Article
from application.validation import NotFoundError,BusinessValidationError
from flask_restful import reqparse
from application.database import db

output_fields={
    "user_id":fields.Integer,
    "username":fields.String,
    "email":fields.String
}
create_user_parser=reqparse.RequestParser()
create_user_parser.add_argument('username')
create_user_parser.add_argument('email')

update_user_parser=reqparse.RequestParser()
update_user_parser.add_argument('email')

class UserAPI(Resource):
    @marshal_with(output_fields)
    def get(self,username):
        print("in get method")
        user1=user.query.filter(user.username==username).first()
        print(user1)
        if user1:
            return user1
        else: 
            raise NotFoundError(status_code=404)
    @marshal_with(output_fields)
    def put(self,username):
        args=update_user_parser.parse_args()
        ema=args.get("email",None)
        if ema is None:
            raise BusinessValidationError(status_code=400, error_code="ABC124", error_message="email is required")
        if "@" not in ema:
            raise BusinessValidationError(status_code=400, error_code="ABC125", error_message="email is invalid")
        user2=user.query.filter(user.email==ema).first()
        if user2:
            raise BusinessValidationError(status_code=400, error_code="ABC128", error_message="duplicate email")
        user4=user.query.filter(user.username==username).first()
        if not user4:
            raise NotFoundError(status_code=404)
        user4.email= ema
        db.session.add(user4)
        db.session.commit()
        return user4
        

    def delete(self,username):
        user3=user.query.filter(user.username==username).first()
        if not user3:
            raise NotFoundError(status_code=404)
        art=Article.query.filter(Article.authors.any(username=username)).all()
        if art and len(art)>0:
            raise BusinessValidationError(status_code=400, error_code="ABC127", error_message="Cannot delete as there are articles written by this user.")
        db.session.delete(user3)
        db.session.commit()
        return "",201

    def post(self):
        args=create_user_parser.parse_args()
        usename=args.get("username",None)
        ema=args.get("email",None)
        
        if usename is None:
            raise BusinessValidationError(status_code=400, error_code="ABC123", error_message="username is required")
        if ema is None:
            raise BusinessValidationError(status_code=400, error_code="ABC124", error_message="email is required")
        if "@" not in ema:
            raise BusinessValidationError(status_code=400, error_code="ABC125", error_message="email is invalid")
        user2=user.query.filter((user.username==usename) | (user.email==ema)).first()
        if user2:
            raise BusinessValidationError(status_code=400, error_code="ABC126", error_message="duplicate user")
        new_user=user(username=usename,email=ema)
        db.session.add(new_user)
        db.session.commit()
        return "",201