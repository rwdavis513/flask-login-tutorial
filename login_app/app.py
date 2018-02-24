from flask_login import LoginManager, login_user, login_required, logout_user
from flask import request, render_template, redirect, url_for, make_response
from flask_app import app, db, init_db
from forms import SignupForm
from models import User
login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/')
def index():
    return "Welcome to Flask"


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if request.method == 'GET':
        return render_template('signup.html', form=form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            if db.session.query(User).filter_by(email=form.email.data).first():
                return "Email address already exists"
            else:
                newuser = User(form.email.data, form.password.data)
                db.session.add(newuser)
                db.session.commit()
                login_user(newuser)
                return "will create user here"
        else:
            return make_response("form not validated", 400)


@app.route('/login', methods=['GET','POST'])
def login():
    form = SignupForm()
    if request.method == 'GET':
        return render_template('login.html', form=form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            user=db.session.query(User).filter_by(email=form.email.data).first()
            if user:
                if user.password == form.password.data:
                    login_user(user)
                    return "User logged in"
                else:
                    return "Wrong password", 400
            else:
                return "user doesn't exist", 400
        else:
            return make_response("form not validated", 400)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return "Logged out"


@login_manager.user_loader
def load_user(email):
    return User.query.filter_by(email = email).first()


@app.route('/protected')
@login_required
def protected():
    return "protected area"


if __name__ == '__main__':
    init_db()
    app.run(port=5000, host='localhost')

