from flask import Flask
from flask_migrate import Migrate

# Use package-style import so this module works when imported as
# `server.app` or via a top-level proxy `app.py`.
from server.models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

# Create all tables when the app is initialized so tests that expect
# database tables to exist can run without requiring separate migrations.
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return '<h1>Flask SQLAlchemy Lab 2</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)
