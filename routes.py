from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app import app, db, bcrypt
from forms import RegistrationForm, LoginForm
from models import *

class UserController:
    
    @staticmethod
    def register(request):
        form = RegistrationForm()

        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            confirm_password = form.confirm_password.data

            # Check if passwords match
            if password != confirm_password:
                flash('Passwords do not match. Please try again.', 'error')

            # Check if email is already in use
            existing_user = User.query.filter_by(email=email).first()
            if existing_user:
                flash('Email is already in use. Please choose a different email.', 'error')

            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

            new_user = User(username=username, email=email, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()

            flash('Registration successful! You can log in now.', 'success')
            return redirect(url_for('login'))

        return render_template('register.html', form=form)

    @staticmethod
    def login(request):
        form = LoginForm()

        if request.method == 'POST' and form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            user = User.query.filter_by(username=username).first()

            if user and bcrypt.check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('dashboard'))
            elif user is None:
                flash("Can't find this username. Please try again.", 'error')
            else:
                flash('Invalid username or password. Please try again.', 'error')

        return render_template('login.html', form=form)


    @staticmethod
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('index'))


@app.route('/Dashboard')
@login_required
def dashboard():
    data_lesson = get_all(Lesson)
    return render_template("dashboard.html", data_lesson=data_lesson, classmeet=get_all(Class))


@app.route("/Learning/<id_lesson>", methods=["GET", "POST"])
@login_required
def lesson(id_lesson):
    return render_template('topics.html', data_topics=get_topics_lesson(id_lesson), data_lesson=Lesson.query.filter_by(id=id_lesson).first())
    

@app.route('/register', methods=['GET', 'POST'])
def register():
    return UserController.register(request)


@app.route('/login', methods=['GET', 'POST'])
def login():
    return UserController.login(request)


@app.route('/logout')
def logout():
    return UserController.logout()


@app.route('/topics')
def topics():
    return get_topics_lesson(id_lesson=20)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


