from flask import make_response, jsonify, abort, request
from sofl import app, db
from sofl.models import User, Question, Answer, Comment
from sofl.errors import error_response, bad_request

# Connection to database before request
@app.before_request
def before_request():
	db.connect()
	db.create_tables([User, Question, Answer], safe = True)

# Closure of database after request
@app.teardown_request
def teardown_request(exc):
	if not db.is_closed():
		db.close()

# URL Endpoints

# Register a user
@app.route('/auth/signup', methods = ['POST'])
def signup_user():
	data = request.get_json() or {}
	if 'username' not in data or 'password' not in data:
		return bad_request('Must include username and password to signup.')
	user = User.get_or_none(User.username == data['username'])
	if user:
		return bad_request('That username is already taken, please use a different one.')
	User.create(username = data['username'], password = data['password'])
	user = User.get(User.username == data['username'])
	response = jsonify(user.to_dict(include_password = False))
	response.status_code = 201
	return response

# Login a user
@app.route('/auth/login', methods = ['POST'])
def login_user():
	data = request.get_json() or {}
	if 'username' not in data or 'password' not in data:
		return bad_request('Must include username and password to login.')
	user = User.get_or_none(User.username == data['username'])
	if not user:
		return bad_request('Username not found. Register to signup.')
	
	response = 'me'
	#response.status_code = 200
	return response

# Fetch all questions
@app.route('/questions', methods = ['GET'])
def fetch_questions():
	questions = Question.select()
	if len(questions) == 0:
		return make_response(404, 'No questions in the database.')
	response = jsonify([question.to_dict() for question in questions])
	response.status_code = 200
	return response

# Post a question
@app.route('/questions', methods = ['POST'])
def post_question():
	Question.create(user = 1,
					title = 'First question',
					body = 'First question body')
	return jsonify(success='trun')

# Fetch a specific question
@app.route('/questions/<questionId>', methods = ['GET'])
def fetch_question():
	return

# Delete a question
@app.route('/questions/<questionId>', methods = ['DELETE'])
def delete_question():
	return

# View the answers to a question
@app.route('/questions/<questionId>/answers', methods = ['GET'])
def view_answers_to_question():
	return

# Post an answer to a question
@app.route('/questions/<questionId>/answers', methods = ['POST'])
def post_answer_to_question():
	return

# Mark an answer as accepted or update an answer
@app.route('/questions/<questionId>/answers/<answerId>', methods = ['PUT'])
def mark_answer_as_accepted_or_deleted():
	return

# Upvote an answer
@app.route('/questions/<questionId>answers/<answerId>', methods = ['PUT'])
def upvote_answer():
	return

# Downvote an answer
@app.route('/questions/<questionId>answers/<answerId>', methods = ['PUT'])
def downvote_answer():
	return

# Fetch all questions posted by the user
@app.route('/users/<userId>/questions', methods = ['GET'])
def fetch_questions_by_user():
	return

# Search for questions
@app.route('/searchforquestion', methods = ['GET'])
def search_for_question():
	return

# View question with most answers
@app.route('/questionwithmostanswers', methods = ['GET'])
def question_with_most_answer():
	return

# Get a specific user
@app.route('/users/<userId>', methods = ['GET'])
def get_specific_user(userId):
	user = User.get_or_none(User.id == userId)
	if user:
		return jsonify(user.to_dict()), 200
	else:
		return error_response(404, 'User with requested ID does not exist.')