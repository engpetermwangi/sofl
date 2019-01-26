from peewee import *
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