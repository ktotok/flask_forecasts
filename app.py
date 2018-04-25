from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

if not db:
    raise SystemExit('DB not loaded')
from config import DevelopmentConfig


app.config.from_object(DevelopmentConfig)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/users/<id>/')
def hello_world(id):
    user = Users.query.get(id)
    print(user.user_email)
    return user.user_email


@app.route('/users/create', methods=['POST'])
def create_user_view():
    if request.form:
        new_user_email = request.form['user_email']
        user_exists = Users.query.filter_by(user_email=new_user_email).first()

        if not user_exists:
            new_user_model = Users(user_email=new_user_email)
            db.session.add(new_user_model)
            db.session.commit()
            created_user = Users.query.filter_by(user_email=new_user_email).first()
            return "New User crested: {} : {}"\
                .format(created_user.id, created_user.user_email)
        return "User already exists {} : {}".format(user_exists.id, user_exists.user_email)


class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_email = db.Column(db.String())

    def __repr__(self):
        return '<id {}>'.format(self.id)

