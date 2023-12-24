from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app import app, db, bcrypt
from forms import RegistrationForm, LoginForm
from models import User

class UserController:
    
    @staticmethod
    def register(request):
        form = RegistrationForm()

        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
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

            new_user = User(email=email, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()

            flash('Registration successful! You can now log in.', 'success')
            return redirect(url_for('login'))

        return render_template('register.html', form=form)

    @staticmethod
    def login(request):
        form = LoginForm()

        print("Mulai\n\n\n")
        if request.method == 'POST' and form.validate_on_submit():
            print("Masuk\n\n\n")
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


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template("dashboard.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    return UserController.register(request)

@app.route('/login', methods=['GET', 'POST'])
def login():
    return UserController.login(request)

@app.route('/logout')
def logout():
    return UserController.logout()
