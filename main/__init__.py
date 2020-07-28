from flask import Flask
from .config import Config
from flask_mongoengine import MongoEngine
from marshmallow import Schema,fields,post_load
from bson import ObjectId

app=Flask(__name__)
app.config.from_object(Config)

db=MongoEngine(app)
Schema.TYPE_MAPPING[ObjectId]=fields.String

from . import views