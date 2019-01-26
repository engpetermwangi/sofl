from flask import make_response, jsonify, abort, request
from sofl import app, db
from sofl.models import User, Question, Answer, Comment

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

# Error handlers
@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'404 error': 'requested resource not found'}))

# URL Endpoints
# Register a user
@app.route('/auth/signup', methods = ['POST'])
def signup_user():
	#user = User.get(User.id == 3)
	#user.delete_instance()
	#User.create(username = 'Petniknker233mnjnjnjjjnnj4red',
	#			password = 'qwerty')
	return jsonify({'users': [user.id for user in User.select()]})

# Login a user
@app.route('/auth/login', methods = ['POST'])
def login_user():
	user = User.get(User.username == 'Peter')
	return jsonify(password = user.password)

# Fetch all questions
@app.route('/questions', methods = ['GET'])
def fetch_questions():
	questions = Question.select()
	if len(questions) == 0:
		abort(404)
	return jsonify({'questions': [question.title for question in Question.select()]}) #jsonify({'questions': questions})

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
@app.route('/questionsbyuser', methods = ['GET'])
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