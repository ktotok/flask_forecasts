from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Users


@app.route('/users/<id>')
def hello_world(id):
    user = Users.query.get(id)
    return user.user_email
