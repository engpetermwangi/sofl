import os
import base64
from peewee import *
from flask import url_for
from datetime import datetime, timedelta
from sofl import db

# Database models

# Base model
class BaseModel(Model):
    class Meta:
        database = db

# User model
class User(BaseModel):
    '''A user has an id, username as the unique identifier and password'''
    username = CharField(null = False, unique = True)
    password = CharField(null = False)
    token = CharField(unique = True)
    token_expiration = DateTimeField()

    def to_dict(self, include_password = False):
        data = {
            'id': self.id,
            'username': self.username,
            'link': url_for('get_specific_user', userId = self.id),
            }
        if include_password:
            data['password'] = self.password
        return data
    
    def get_token(self, expires_in = 3600):
        now = datetime.utcnow()
        if self.token and self.token_expiration > now + timedelta(seconds = 1):
            return self.token
        self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
        self.token_expiration = now + timedelta(seconds = expires_in)
        return self.token
    
    def revoke_token(self):
        self.token_expiration = datetime.utcnow() - timedelta(seconds=1)
    
    @staticmethod
    def check_token(token):
        user = User.get_or_none(User.token = token)
        if user is None or user.token_expiration < datetime.utcnow():
            return None
        return user

# Question model
class Question(BaseModel):
	'''A question has an id, a user(User) as a foreign key, a title and a body'''
	user = ForeignKeyField(User, backref = 'questions', null = False)
	title = CharField(null = False)
	body = CharField(null = False)

# Answer model
class Answer(BaseModel):
	'''An answer has an id, two foreign keys, a user(User) and question(Question) as well as a body.'''
	user = ForeignKeyField(User, backref = 'answers', null = False)
	question = ForeignKeyField(Question, backref = 'answers', null = False)
	body = CharField(null = False)

# Comment model
class Comment(BaseModel):
	'''A comment has an id and two foreign keys, user(User) and the answer(Answer).'''
	user = ForeignKeyField(User, backref = 'comments', null = False)
	answer = ForeignKeyField(Answer, backref = 'comments', null = False)