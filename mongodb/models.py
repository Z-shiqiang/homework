import mongoengine as mongoengine
from django.db import models

# Create your models here.

class User(mongoengine.Document):
    name = mongoengine.StringField(max_length=55)
    age = mongoengine.IntField(default=20)
    grade = mongoengine.StringField(max_length=55)
