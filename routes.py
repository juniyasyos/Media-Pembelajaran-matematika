from flask import render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from app import app, db, bcrypt
from datetime import datetime, timedelta
from forms import RegistrationForm, LoginForm
from models import *
from functools import reduce
from sqlalchemy import func, Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
# from icecream import ic

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
            new_user = User(username=username, email=email, password=hashed_password, role=role, point=0)
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
    if current_user.role_id == 2:
        return render_template(
            "dashboard.html", 
            data_lesson=data_lesson, 
            classmeet=get_all(Class), 
            post_test_user=all_modul_user, 
            data_topics=get_all_category_topics(), 
            user=current_user,
            modul_user=modul_user,
            data_quiz=get_count_category_lesson(),
            quiz_user=len(get_user_quiz_statuses(user_id=current_user.id)),
            # all_modul_user="",
            # all_user_quiz_status="",
            all_user="")
    else:
        return render_template(
            "dashboard.html", 
            data_lesson=data_lesson, 
            classmeet=get_all(Class), 
            post_test_user=all_modul_user, 
            data_topics=get_all_category_topics(), 
            user=current_user,
            modul_user=modul_user,
            data_quiz=get_count_category_lesson(),
            quiz_user=len(get_user_quiz_statuses(user_id=current_user.id)),
            all_modul_user=get_all_user_post_test_statuses(),   
            all_user_quiz_status=get_all_user_quiz_statuses(),
            all_user=User.query.filter_by(role_id=2).count())


@app.route("/Learning/get='<lesson_id>'", methods=["GET", "POST"])
@login_required
def lesson(lesson_id):
    all_modul_user = get_user_post_test_statuses(user_id=current_user.id)
    data_lesson = Lesson.query.filter_by(id=lesson_id).first()
    data_quiz = Quiz.query.filter_by(quiz_id=data_lesson.quiz_id).first()
    
    return render_template(
        'lesson.html', 
        data_topics=get_topics_lesson(lesson_id), 
        data_lesson=data_lesson,
        post_test_user=all_modul_user, 
        data_lesson_user=get_all_category_topics(),
        all_modul_user=get_all_user_post_test_statuses(),
        all_user_quiz_status=get_all_user_quiz_statuses(),
        user=current_user,
        data_quiz=data_quiz)

@app.route("/Learning/get=<lesson_id>/quizz=<quiz_id>", methods=["GET", "POST"])
@login_required
def quiz(lesson_id, quiz_id):
    return render_template('exercise.html', data_question=get_questions_data_by_quiz_id(quiz_id=quiz_id), count_question=Question.query.filter_by(quiz_id=quiz_id).count(), quiz_id=quiz_id)


@app.route("/Learning/get='<lesson_id>'/topics=<src_topics>", methods=["GET", "POST"])
@login_required
def topics(lesson_id, src_topics):
    data_topics = Topics.query.filter_by(src_topics=src_topics).first()
    return render_template(f'topics/{src_topics}', data_topics=data_topics)


@app.route("/Learning/get='<lesson_id>'/csoal=<src>", methods=["GET", "POST"])
@login_required
def csoal(lesson_id, src):
    data_lesson = Lesson.query.filter_by(src=src).first()
    return render_template(f'contoh_soal/{src}')


@app.route("/Learning/get='<lesson_id>'/studikasus=<src>", methods=["GET", "POST"])
@login_required
def studi_kasus(lesson_id, src):
    data_lesson = Lesson.query.filter_by(src=src).first()
    return render_template(f'studi_kasus/{src}')


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

        if existing_data and current_user.role_id == 2:
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


@app.route('/update_quiz/<quiz_id>', methods=['POST'])
@login_required
def handle_form_submission(quiz_id):
    try:
        data = request.json
        quiz = Quiz.query.filter_by(quiz_id=quiz_id).first()

        if not quiz:
            return jsonify({'error': 'Quiz not found'}), 404  # Return 404 Not Found if the quiz is not found

        # Mendapatkan data tanggal dan waktu yang dikirimkan dari client
        client_start_datetime_utc = datetime.fromisoformat(data.get('startDateTime'))
        client_end_datetime_utc = datetime.fromisoformat(data.get('endDateTime'))

        # Konversi waktu dari UTC ke zona waktu lokal (Western Indonesia Time)
        client_start_datetime_local = client_start_datetime_utc + timedelta(hours=7)
        client_end_datetime_local = client_end_datetime_utc + timedelta(hours=7)

        # Assign waktu lokal ke objek quiz
        quiz.waktu_mulai = client_start_datetime_local
        quiz.waktu_selesai = client_end_datetime_local
        db.session.commit()

        return jsonify({'message': 'Update Berhasil'})

    except Exception as e:
        # Tangkap kesalahan umum jika terjadi
        db.session.rollback()  # Rollback the changes in case of an error
        return jsonify({'error': str(e)}), 500  # Return 500 Internal Server Error


@app.route('/submit-answers/<quiz_id>', methods=['POST','GET'])
@login_required
def submit_answers(quiz_id):
    data = request.get_json()
    user_answers = data.get('selectedChoices')
    user_answers_text = data.get('selectedChoicesText')
    
    # Ambil data kuis dari database
    quiz = Quiz.query.filter_by(quiz_id=quiz_id).first()

    # Hitung skor
    total_score = 0
    total_questions = 0
    correct_answer_user = 0

    for question in quiz.questions:
        # Ambil jawaban yang benar dari opsi jawaban
        correct_answer = next((option.teks_opsi for option in question.options if option.jawaban_benar), None)

        # Bandingkan jawaban pengguna dengan jawaban yang benar
        user_answer = user_answers_text.get(f'{total_questions + 1}')

        # Periksa apakah pengguna telah memberikan jawaban
        if user_answer is not None:
            total_questions += 1

            # Bandingkan jawaban pengguna dengan jawaban yang benar
            if user_answer == correct_answer:
                total_score += question.point
                correct_answer_user += 1

    # Hitung skor rata-rata jika ada pertanyaan yang dijawab
    # average_score = total_score / total_questions if total_questions > 0 else 0
    
    # # Konversi estimasi waktu dari milidetik ke menit dan detik
    # estimated_time_in_seconds = data['estimatedTime'] // 1000
    # minutes = estimated_time_in_seconds // 60
    # seconds = estimated_time_in_seconds % 60

    # # Tambahkan informasi waktu ke data
    # data['estimatedTimeMinutes'] = minutes
    # data['estimatedTimeSeconds'] = seconds

    check_status_quiz = UserQuizStatus.query.filter_by(user_id=current_user.id, quiz_id=quiz.quiz_id).first()

    if check_status_quiz:
        # Kirim data JSON sebagai respons
        response_data = {
            'user': current_user.serialize(),
            'estimatedTime': data.get('estimatedTime'),
            'score': total_score,
            'message': "Anda sudah mengerjakan kuis, data lama tidak akan diperbaharui",
            'totalAnswered': total_questions,
            'correctAnswers': correct_answer_user,
            'incorrectAnswers': total_questions - correct_answer_user
        }
        return jsonify(response_data)
    else:
        if current_user.role_id == 2:
            new_user_quiz = UserQuizStatus(user_id=current_user.id, quiz_id=quiz_id, score=total_score, time=data.get('estimatedTime'), date=datetime.now())
            current_user.point += int(total_score) 
            db.session.commit()
            db.session.add(new_user_quiz)
            db.session.commit()
            
            # Kirim data JSON sebagai respons
            response_data = {
                'user': current_user.serialize(),
                'estimatedTime': data.get('estimatedTime'),
                'score': total_score,
                'message': "Data Pengerjaan Kuis Disimpan",
                'totalAnswered': total_questions,
                'correctAnswers': total_score,
                'incorrectAnswers': total_questions - correct_answer_user
            }
        else:
            # Kirim data JSON sebagai respons
            response_data = {
                'user': current_user.serialize(),
                'estimatedTime': data.get('estimatedTime'),
                'score': total_score,
                'message': "Data tidak di simpan, Anda bukan siswa",
                'totalAnswered': total_questions,
                'correctAnswers': total_score,
                'incorrectAnswers': total_questions - correct_answer_user
            }
        return jsonify(response_data), 404


@app.route("/Leaderboard", methods=["GET", "POST"])
@login_required
def rank():
    return render_template('leaderboard.html', all_user=User.query.filter_by(role_id=2).order_by(User.point.desc()).all())


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