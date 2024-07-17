from mongoengine import Document,StringField,ListField,ReferenceField,FloatField,BooleanField

class Products (Document):
    name = StringField(required=True,unique=True)
    price = FloatField(required=True)

class Category (Document):
    name = StringField(required=True,unique=True)
    products = ListField(ReferenceField(Products),default=list)

class Users (Document):
    username = StringField(required=True,unique=True)
    password = StringField(required=True)
    isAdmin = BooleanField(default=False)
    cart = ListField(ReferenceField(Products),default=list)