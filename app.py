from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_compress import Compress
from urllib.parse import quote_plus

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/medpem_mtk'


# # Ganti informasi ini sesuai dengan informasi dari link phpMyAdmin
# db_host = 'iix1533.idcloudhost.com'
# db_port = 3306  # Ganti dengan port yang sesuai
# db_name = 'nwwbgeal_math-sip'
# db_user = 'nwwbgeal_ilyas'
# db_password = 'RmbXN_BRe3HA5PN'  # Isi dengan kata sandi yang sesuai

# # Membuat URI SQLAlchemy
# uri = f"mysql+pymysql://{db_user}:{quote_plus(db_password)}@{db_host}:{db_port}/{db_name}"

# Konfigurasi Flask
# app.config['SQLALCHEMY_DATABASE_URI'] = uri


compress = Compress(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


from routes import *

if __name__ == '__main__':
    app.run(debug=True)
