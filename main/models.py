from main import db
from marshmallow import fields,Schema

#######################################
########## The Author Model############
######################################

class Author(db.Document):
    name=db.StringField()
    specialization=db.StringField()

#################################
#### The Output Schema ##########
#################################

class AuthorSchema(Schema):
    name=fields.String(required=True)
    specialization=fields.String(required=True)




