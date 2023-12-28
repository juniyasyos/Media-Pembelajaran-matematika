from app import db, login_manager
from datetime import datetime
from flask_login import UserMixin

class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(50), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    def serialize(self):
        return {
            'id': self.id,
            'role_name': self.role_name,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    activation_code = db.Column(db.Boolean, default=False, nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    role = db.relationship('Role', backref='users')
    
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'activation_code': self.activation_code,
            'role': self.role.serialize() if self.role else None
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
    quiz = db.relationship('Question', backref='lessons')
    
    def serialize(self):
        return {
            'id': self.id,
            'class_id': self.class_id,
            'quiz_id': self.quiz_id,
            'lesson_name': self.lesson_name,
            'class_': self.class_.serialize() if self.class_ else None,
            'quiz': self.quiz.serialize() if self.quiz else None
        }


class Topics(db.Model):
    __tablename__ = 'topics'
    id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.id'), nullable=False)
    topics_name = db.Column(db.String(255), nullable=False)
    lesson = db.relationship('Lesson', backref='topics')
    
    def serialize(self):
        return {
            'id': self.id,
            'lesson_id': self.lesson_id,
            'topics_name': self.topics_name,
            'lesson': self.lesson.serialize() if self.lesson else None
        }


class Explanation(db.Model):
    __tablename__ = 'explanation'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(255))
    video = db.Column(db.String(255))
    priority = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    created_by = db.Column(db.String(255), nullable=False)
    topics_id = db.Column(db.Integer, db.ForeignKey('topics.id'), nullable=False)
    topics = db.relationship('Topics', backref='explanations')
    
    def serialize(self):
        return {
            'id': self.id,
            'text': self.text,
            'image': self.image,
            'video': self.video,
            'priority': self.priority,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'created_by': self.created_by,
            'topics_id': self.topics_id,
            'topics': self.topics.serialize() if self.topics else None
        }


class TypeQuestion(db.Model):
    __tablename__ = 'type_question'
    id = db.Column(db.Integer, primary_key=True)
    type_question_name = db.Column(db.String(255), nullable=False)
    
    def serialize(self):
        return {
            'id': self.id,
            'type_question_name': self.type_question_name
        }



class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(255), nullable=False)
    id_type = db.Column(db.Integer, db.ForeignKey('type_question.id'), nullable=False)
    type_question = db.relationship('TypeQuestion', backref='questions')
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'id_type': self.id_type,
            'type_question': self.type_question.serialize() if self.type_question else None
        }


class PathQuestion(db.Model):
    __tablename__ = 'path_question'
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(255))
    video = db.Column(db.String(255))
    text = db.Column(db.Text)
    type_question_id = db.Column(db.Integer, db.ForeignKey('type_question.id'), nullable=False)
    priority = db.Column(db.Integer)
    question_type = db.Column(db.String(20))
    type_question = db.relationship('TypeQuestion', backref='path_questions')
    
    def serialize(self):
        return {
            'id': self.id,
            'image': self.image,
            'video': self.video,
            'text': self.text,
            'type_question_id': self.type_question_id,
            'priority': self.priority,
            'question_type': self.question_type,
            'type_question': self.type_question.serialize() if self.type_question else None
        }


class QuestionMultipleChoice(db.Model):
    __tablename__ = 'question_multiplechoice'
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.String(255))
    path_question_id = db.Column(db.Integer, db.ForeignKey('path_question.id'), nullable=False)
    path_question = db.relationship('PathQuestion', backref='question_multiplechoices')
    
    def serialize(self):
        return {
            'id': self.id,
            'answer': self.answer,
            'path_question_id': self.path_question_id,
            'path_question': self.path_question.serialize() if self.path_question else None
        }


class QuestionEssai(db.Model):
    __tablename__ = 'question_essai'
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.Text)
    path_question_id = db.Column(db.Integer, db.ForeignKey('path_question.id'), nullable=False)
    path_question = db.relationship('PathQuestion', backref='question_essais')
    
    def serialize(self):
        return {
            'id': self.id,
            'answer': self.answer,
            'path_question_id': self.path_question_id,
            'path_question': self.path_question.serialize() if self.path_question else None
        }


class UserLesson(db.Model):
    __tablename__ = 'user_lesson'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.id'), primary_key=True)
    progress = db.Column(db.Integer)
    user = db.relationship('User', backref='user_lessons')
    lesson = db.relationship('Lesson', backref='user_lessons')
    
    def serialize(self):
        return {
            'user_id': self.user_id,
            'lesson_id': self.lesson_id,
            'progress': self.progress,
            'user': self.user.serialize() if self.user else None,
            'lesson': self.lesson.serialize() if self.lesson else None
        }


class UserTopics(db.Model):
    __tablename__ = 'user_topics'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    topics_id = db.Column(db.Integer, db.ForeignKey('topics.id'), primary_key=True)
    status_read = db.Column(db.String(255))
    user = db.relationship('User', backref='user_topics')
    topics = db.relationship('Topics', backref='user_topics')
    
    def serialize(self):
        return {
            'user_id': self.user_id,
            'topics_id': self.topics_id,
            'status_read': self.status_read,
            'user': self.user.serialize() if self.user else None,
            'topics': self.topics.serialize() if self.topics else None
        }


class UserQuestion(db.Model):
    __tablename__ = 'user_question'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), primary_key=True)
    score = db.Column(db.Integer)
    user = db.relationship('User', backref='user_questions')
    question = db.relationship('Question', backref='user_questions')
    
    def serialize(self):
        return {
            'user_id': self.user_id,
            'question_id': self.question_id,
            'score': self.score,
            'user': self.user.serialize() if self.user else None,
            'question': self.question.serialize() if self.question else None
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