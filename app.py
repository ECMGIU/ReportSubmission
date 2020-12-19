import os
from datetime import datetime

from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)


class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(8))
    title = db.Column(db.String(50))
    ticker = db.Column(db.String(4))
    date = db.Column(db.DateTime(), default=datetime.utcnow)
    team_id = db.Column(db.Integer, db.ForeignKey('team.name'))


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    manager = db.Column(db.String(8))
    color = db.Column(db.String(12))
    reports = db.relationship('Report', backref='team', lazy='dynamic')


@app.route('/')
def list_reports():
    reports = Report.query.all()
    return render_template('list_reports.html', reports=reports)


if __name__ in '__main__':
    app.run()
