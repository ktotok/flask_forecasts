from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

if not db:
    raise SystemExit('DB not loaded')
from config import DevelopmentConfig
from models import Users

app.config.from_object(DevelopmentConfig)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/users/<id>/')
def hello_world(id):
    user = Users.query.get(id)
    return user.user_email


@app.route('/users/create/')
def create_user_view():
    # todo create user with email form post body
    pass
