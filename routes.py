from flask import render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from app import app, db, bcrypt
from forms import RegistrationForm, LoginForm
from models import *
from functools import reduce
from sqlalchemy import func, Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

class UserController:
    @staticmethod
    def register(request):
        form = RegistrationForm()

        if form.validate_on_submit():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            confirm_password = form.confirm_password.data
            user_type = form.user_type.data
            token = form.token.data

            # Check if passwords match
            if password != confirm_password:
                flash('Passwords do not match. Please try again.', 'error')
                return redirect(url_for('register'))

            # Check if email is already in use
            existing_user = User.query.filter_by(email=email).first()
            if existing_user:
                flash('Email is already in use. Please choose a different email.', 'error')
                return redirect(url_for('register'))

            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')


            # Check if the user type is 'guru' or 'admin'
            if user_type in ['guru', 'admin']:
                # Query the role based on the user type
                role = Role.query.filter_by(role_name=user_type).first()

                if not role or role.token != int(token):
                    flash('Invalid token. Please enter a valid token.', 'error')
                    return redirect(url_for('register'))
            else:
                # If the user type is not 'guru' or 'admin', set a default role (e.g., 'siswa')
                role = Role.query.filter_by(role_name='siswa').first()

            # Create a new user with the obtained role
            new_user = User(username=username, email=email, password=hashed_password, role=role)
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
            if user is None:
                user = User.query.filter_by(email=username).first()

            if user and bcrypt.check_password_hash(user.password, password):
                login_user(user)
                LOGIN = True
                return redirect(url_for('dashboard'))
            elif user is None:
                flash("Can't find this username or email. Please try again or signup", 'error')
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
    all_modul_user = get_user_post_test_statuses(user_id=current_user.id)
    modul_user = sum(len(lesson) for lesson in all_modul_user.values())
    return render_template(
        "dashboard.html", 
        data_lesson=data_lesson, 
        classmeet=get_all(Class), 
        post_test_user=all_modul_user, 
        data_topics=get_all_category_topics(), 
        user=current_user,
        modul_user=modul_user,
        data_quiz=get_count_category_lesson(),
        quiz_user=len(get_user_quiz_statuses(user_id=current_user.id)))

@app.route("/Learning/get='<lesson_id>'", methods=["GET", "POST"])
@login_required
def lesson(lesson_id):
    all_modul_user = get_user_post_test_statuses(user_id=current_user.id)
    return render_template(
        'lesson.html', 
        data_topics=get_topics_lesson(lesson_id), 
        data_lesson=Lesson.query.filter_by(id=lesson_id).first(),
        post_test_user=all_modul_user, 
        data_lesson_user=get_all_category_topics())


@app.route("/Learning/get=<lesson_id>/quizz=<quiz_id>", methods=["GET", "POST"])
@login_required
def quiz(lesson_id, quiz_id):
    return render_template('exercise.html', data_question=get_questions_data_by_quiz_id(quiz_id=quiz_id))


@app.route("/Learning/get='<lesson_id>'/topics=<src_topics>", methods=["GET", "POST"])
@login_required
def topics(lesson_id, src_topics):
    data_topics = Topics.query.filter_by(src_topics=src_topics).first()
    return render_template(f'topics/{src_topics}', data_topics=data_topics)


@app.route('/save_progress', methods=['POST'])
@login_required
def save_progress():
    try:
        topics_id = int(request.form.get('topics_id'))
        user_id = int(current_user.id)
        reading_duration = int(request.form.get('reading_duration'))
        # print("masuk")

        # Check if data already exists
        existing_data = UserPostTest.query.filter_by(topics_id=topics_id, user_id=user_id).first()

        if existing_data:
            # print("ada")
            # Update reading_duration
            existing_data.reading_duration += reading_duration
            response = {'status': 'success', 'message': 'Data berhasil diupdate.'}
        else:
            # Save new data
            new_data = UserPostTest(topics_id=topics_id, user_id=user_id, reading_duration=reading_duration)
            topics = Topics.query.filter_by(id=topics_id).first()
            current_user.point += int(topics.poin)
            
            db.session.commit()
            db.session.add(new_data)
            db.session.commit()

            response = {'status': 'success', 'message': 'Data berhasil disimpan.'}

        return jsonify(response), 200

    except Exception as e:
        # print("gagal = ", e)
        response = {'status': 'error', 'message': 'Gagal menyimpan progress.'}
        return jsonify(response), 500


@app.route("/Profile", methods=["GET", "POST"])
@login_required
def profile():
    return render_template('profil.html', user=current_user)
    

@app.route('/register', methods=['GET', 'POST'])
def register():
    return UserController.register(request)


@app.route('/login', methods=['GET', 'POST'])
def login():
    return UserController.login(request)


@app.route('/logout')
def logout():
    return UserController.logout()

# Handler untuk error 404
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404