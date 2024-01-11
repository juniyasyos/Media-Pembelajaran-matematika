from app import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from sqlalchemy import func, Column, Integer, Text, ForeignKey, String, DateTime, Enum, Boolean, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import json


class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(50), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    token = db.Column(db.Integer, nullable=False)
    
    def serialize(self):
        return {
            'id': self.id,
            'role_name': self.role_name,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'token' : self.token
        }


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    activation_code = db.Column(db.Boolean, default=False, nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    role = db.relationship('Role', backref='users')
    point = db.Column(db.Integer, nullable=False)
    
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'activation_code': self.activation_code,
            'role': self.role.serialize() if self.role else None,
            'point' : self.point
        }


class Semester(db.Model):
    __tablename__ = 'semester'
    id = db.Column(db.Integer, primary_key=True)
    semester_name = db.Column(db.String(255), nullable=False)
    
    def serialize(self):
        return {
            'id': self.id,
            'semester_name': self.semester_name
        }
        

class Bab(db.Model):
    __tablename__ = 'bab'

    id = db.Column(db.Integer, primary_key=True)
    chapter_name = db.Column(db.String(255), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'chapter_name': self.chapter_name,
        }


class Class(db.Model):
    __tablename__ = 'class'
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(255), nullable=False)
    semester_id = db.Column(db.Integer, db.ForeignKey('semester.id'), nullable=False)
    semester = db.relationship('Semester', backref='classes')
    
    def serialize(self):
        return {
            'id': self.id,
            'class_name': self.class_name,
            'semester_id': self.semester_id,
            'semester': self.semester.serialize() if self.semester else None
        }


class Lesson(db.Model):
    __tablename__ = 'lesson'
    id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey('class.id'), nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
    lesson_name = db.Column(db.String(255), nullable=False)
    class_ = db.relationship('Class', backref='lessons')
    # quiz = db.relationship('quiz', backref='lessons')
    
    def serialize(self):
        return {
            'id': self.id,
            'class_id': self.class_id,
            'quiz_id': self.quiz_id,
            'lesson_name': self.lesson_name,
            'class_': self.class_.serialize() if self.class_ else None,
            # 'quiz': self.quiz.serialize() if self.quiz else None
        }


class Topics(db.Model):
    __tablename__ = 'topics'
    id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.id'), nullable=False)
    topics_name = db.Column(db.String(255), nullable=False)
    lesson = db.relationship('Lesson', backref='topics')
    bab_id = db.Column(db.Integer)
    poin = db.Column(db.Integer)
    src_topics = db.Column(db.String(255), nullable=False)
    
    def serialize(self):
        return {
            'id': self.id,
            'lesson_id': self.lesson_id,
            'topics_name': self.topics_name,
            'lesson': self.lesson.serialize() if self.lesson else None,
            'bab_id': self.bab_id,
            'poin' : self.poin,
            'src_topics' : self.src_topics
        }


class UserPostTest(db.Model):
    __tablename__ = 'user_topic_status'

    id = db.Column(db.Integer, primary_key=True)
    topics_id = db.Column(db.Integer, db.ForeignKey('topics.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    reading_duration = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'topics_id': self.topics_id,
            'user_id': self.user_id,
            'reading_duration': self.reading_duration
        }


class UserQuizStatus(db.Model):
    __tablename__ = 'user_quiz_status'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    quiz_id = Column(Integer, ForeignKey('quiz.quiz_id'), nullable=False)
    score = Column(Integer)
    time = Column(Integer)
    date = Column(Date)

    user = relationship('User', backref='user_quiz_statuses')
    quiz = relationship('Quiz', backref='user_quiz_statuses')


class Quiz(db.Model):
    __tablename__ = 'quiz'

    quiz_id = Column(Integer, primary_key=True, autoincrement=True)
    judul = Column(Text)
    deskripsi = Column(Text)
    waktu_mulai = Column(DateTime)
    waktu_selesai = Column(DateTime)
    tipe = Column(Enum('latihan', 'kuis'))

    questions = relationship('Question', back_populates='quiz')

    def serialize(self):
        return {
            'quiz_id': self.quiz_id,
            'judul': self.judul,
            'deskripsi': self.deskripsi,
            'waktu_mulai': self.waktu_mulai.strftime('%Y-%m-%d %H:%M:%S') if self.waktu_mulai else None,
            'waktu_selesai': self.waktu_selesai.strftime('%Y-%m-%d %H:%M:%S') if self.waktu_selesai else None,
            'tipe': self.tipe,
            'questions': [question.serialize() for question in self.questions]
        }

class Question(db.Model):
    __tablename__ = 'question'

    question_id = Column(Integer, primary_key=True, autoincrement=True)
    quiz_id = Column(Integer, ForeignKey('quiz.quiz_id'))
    teks_pertanyaan = Column(Text)
    tipe_pertanyaan = Column(Enum('pilihan_ganda', 'essai'))
    point = Column(Integer, nullable=False)

    quiz = relationship('Quiz', back_populates='questions', primaryjoin="Question.quiz_id==Quiz.quiz_id")
    options = relationship('AnswerOption', back_populates='question')

    def serialize(self):
        return {
            'question_id': self.question_id,
            'quiz_id': self.quiz_id,
            'teks_pertanyaan': self.teks_pertanyaan,
            'tipe_pertanyaan': self.tipe_pertanyaan,
            'options': [option.serialize() for option in self.options]
        }

class AnswerOption(db.Model):
    __tablename__ = 'answeroption'

    option_id = Column(Integer, primary_key=True, autoincrement=True)
    question_id = Column(Integer, ForeignKey('question.question_id'))
    teks_opsi = Column(Text)
    jawaban_benar = Column(Boolean)

    question = relationship('Question', back_populates='options', primaryjoin="AnswerOption.question_id==Question.question_id")

    def serialize(self):
        return {
            'option_id': self.option_id,
            'question_id': self.question_id,
            'teks_opsi': self.teks_opsi,
            'jawaban_benar': self.jawaban_benar
        }


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def get_all(entity):
    all_entities = entity.query.all()
    return [entity.serialize() for entity in all_entities]


def get_topics_lesson(id_lesson):
    lesson_topics = Topics.query.filter_by(lesson_id=id_lesson).all()
    return [topics.serialize() for topics in lesson_topics]


def get_explanation_topics(id_topics):
    explanation_topics = Explanation.query.filter_by(topics_id=id_topics).all()
    return [explanation.serialize() for explanation in explanation_topics]


def get_user_post_test_statuses(user_id):
    data_user = UserPostTest.query.filter_by(user_id=user_id).all()

    # Create a dictionary to store filtered topics for each lesson_id
    filtered_topics_dict = {}

    for data in data_user:
        topics_id = data.topics_id
        lesson_id = None

        # Retrieve lesson_id based on topics_id
        topics = Topics.query.filter_by(id=topics_id).first()
        if topics:
            lesson_id = topics.lesson_id

        if lesson_id is not None:
            # Check if the lesson_id is already in the dictionary
            if lesson_id not in filtered_topics_dict:
                # If not, add an empty list for that lesson_id
                filtered_topics_dict[lesson_id] = []

            # Append the topics_id to the corresponding lesson_id in the dictionary
            filtered_topics_dict[lesson_id].append(topics_id)

    return filtered_topics_dict


def get_all_user_post_test_statuses():
    data_user = UserPostTest.query.all()
    data_topics = get_all_category_topics()

    # Create a dictionary to store filtered topics for each lesson_id
    filtered_topics_dict = {}

    for data in data_user:
        data_posttest_user = get_user_post_test_statuses(data.user_id)
        data_user_spec = User.query.filter_by(id=data.user_id).first()
        topics_id = data.topics_id
        lesson_id = None

        topics = Topics.query.filter_by(id=topics_id).first()
        if topics:
            lesson_id = topics.lesson_id

        if lesson_id is not None:
            if lesson_id not in filtered_topics_dict:
                filtered_topics_dict[lesson_id] = []
            if (len(data_posttest_user[lesson_id]) == data_topics[lesson_id]+1) and data.user_id not in filtered_topics_dict[lesson_id] and data_user_spec.role_id == 2:
                filtered_topics_dict[lesson_id].append(data.user_id)

    return filtered_topics_dict


def get_user_quiz_statuses(user_id):
    data_user = UserQuizStatus.query.filter_by(user_id=user_id).all()

    # Create a dictionary to store filtered quiz for each lesson_id
    filtered_quiz_dict = {}

    for data in data_user:
        quiz_id = data.quiz_id
        lesson_id = None

        lesson = Lesson.query.filter_by(quiz_id=quiz_id).first()
        if lesson:
            lesson_id = lesson.id

        if lesson_id is not None:
            # Check if the lesson_id is already in the dictionary
            if lesson_id not in filtered_quiz_dict:
                # If not, add an empty list for that lesson_id
                filtered_quiz_dict[lesson_id] = []

            # Append the quiz_id to the corresponding lesson_id in the dictionary
            filtered_quiz_dict[lesson_id].append(quiz_id)

    return filtered_quiz_dict


def get_all_user_quiz_statuses():
    data_all_user = UserQuizStatus.query.all()
    
    filtered_topics_dict = {}

    for data in data_all_user:
        data_user_spec = User.query.filter_by(id=data.user_id).first()
        data_lesson = Lesson.query.filter_by(quiz_id=data.quiz_id).first()

        if data_lesson is not None:
            if data_lesson.id not in filtered_topics_dict:
                filtered_topics_dict[data_lesson.id] = []
            if data_user_spec.role_id == 2:
                filtered_topics_dict[data_lesson.id].append(data.user_id)

    return filtered_topics_dict


def get_all_category_topics():
    data_topics = Topics.query.all()
    
    category_topics = {}
    for topic in data_topics:
        if topic.lesson_id not in category_topics:
            category_topics[topic.lesson_id] = 0
        else:
            category_topics[topic.lesson_id] += 1
    return category_topics


def get_count_category_lesson():
    data_lesson = Lesson.query.all()
    
    category_lesson = {}
    for lesson in data_lesson:
        if lesson.class_id not in category_lesson:
            category_lesson[lesson.class_id] = 0
        else:
            category_lesson[lesson.class_id] += 1
    return category_lesson
        

def get_questions_data_by_quiz_id(quiz_id):
    quiz = Quiz.query.filter_by(quiz_id=quiz_id).first()

    if not quiz:
        return None

    questions = Question.query.filter_by(quiz_id=quiz_id).all()

    questions_data = []
    for question in questions:
        choices = [f"{option.teks_opsi}" for idx, option in enumerate(question.options)]
        questions_data.append({
            "number": question.question_id,
            "text": question.teks_pertanyaan,
            "choices": choices
        })

    # Menghasilkan string JSON dari data pertanyaan
    json_data = json.dumps(questions_data)

    return json_data