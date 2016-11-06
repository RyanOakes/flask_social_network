#Setup that virtual env yo
pip install flask
pip install peewee

#Git
git init
echo .DS_Store > .gitignore
echo .envrc >> .gitignore
echo .direnv >> .gitignore
echo __pycache__ >> .gitignore
echo *.pyc >> .gitignore
echo .env >> .gitignore
echo db.sqlite3 >> ../.gitignore




# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # BASICS # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


pip install flask
pip install flask_script
pip install flask-bootstrap
pip install flask-moment
pip install flask-wtf


from flask import Flask
from flask_script import Manager
from flask import request

app = Flask(__name__)
manager = Manager(app)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # BASICS # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# // SIMPLE RESPONSE
@app.route('/')
def index():
    return '<h1>CATS DROOL</h1>'


# // USING CONTEXTS
@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    cookie = request.headers.get('Cookie')
    return '<p>Your browser is %s and your cookie is: %s</p>' %(user_agent, cookie)


# // RETURNING STATUS CODE
@app.route('/')
def index():
    return '<h1>Bad Request</h1>', 400


# // USING DYNAMIC ROUTING
@app.route('/user/<name>')
def user(name):
    return '<h1>Hi %s!</h1>' %(name)


# // RETURNING RESPONSE OBJECT
@app.route('/')
def index():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response


# // REDIRECTS
@app.route('/)
def user(name):
    return redirect('http://www.example')


# // ABORT FUNCTION - USED FOR ERROR HANDLING
@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, %s</h1>' %(user.name)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # TEMPLATES # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #




if __name__ == '__main__':
    # app.run(debug=True)

    # // If using flask-script and Manager for CLI server manipulation
    manager.run()
