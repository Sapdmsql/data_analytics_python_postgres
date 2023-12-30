import os
from datetime import datetime

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='static')

app.config.update(
    SQLALCHEMY_DATABASE_URI='postgresql://app_user:app_password@db:5432/app',
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

# Initialize the database connection
db = SQLAlchemy(app)

# Enable Flask-Migrate commands "flask db init/migrate/upgrade" to work
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run()
