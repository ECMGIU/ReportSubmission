import os

from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), index=True)
    title = db.Column(db.String(), index=True)
    ticker = db.Column(db.String(), index=True)
    date = db.Column(db.String(), index=True)


@app.route('/')
def list_reports():
    # reports will be replaced with a database query eventually
    reports = [
        {
            'ticker': 'AGCO',
            'title': 'Opportunities in AgTech',
            'username': 'wbfletch',
            'url': 'https://wadeflet.ch'
        },
        {
            'ticker': 'INDA',
            'title': 'Indian Tech poised for major gains',
            'username': 'wbfletch',
            'url': 'https://wadeflet.ch'
        }
    ]
    return render_template('list_reports.html', reports=reports)


if __name__ in '__main__':
    app.run()
