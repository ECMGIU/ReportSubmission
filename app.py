import os
from datetime import datetime

import boto3 as boto3
from flask import Flask, render_template, request, url_for, redirect
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['S3_BUCKET'] = os.environ.get('BUCKETEER_BUCKET_NAME')
app.config['S3_KEY'] = os.environ.get('BUCKETEER_AWS_ACCESS_KEY_ID')
app.config['S3_SECRET'] = os.environ.get('BUCKETEER_AWS_SECRET_ACCESS_KEY')

db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)
s3 = boto3.client(
    "s3",
    aws_access_key_id=app.config['S3_KEY'],
    aws_secret_access_key=app.config['S3_SECRET']
)


def upload_file_to_s3(file, name):
    s3.upload_fileobj(
        file,
        app.config['S3_BUCKET'],
        name,
        ExtraArgs={
            "ACL": "public-read",
            "ContentType": file.content_type
        }
    )

    return 'http://{}.s3.amazonaws.com/{}'.format(app.config['S3_BUCKET'], name)


class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(8))
    title = db.Column(db.String(50))
    ticker = db.Column(db.String(4))
    date = db.Column(db.DateTime(), default=datetime.utcnow)
    downloads = db.Column(db.Integer)
    url = db.Column(db.String)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))

    def __repr__(self):
        return f'<Report {self.title} by {self.username}>'


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    manager = db.Column(db.String(8))
    color = db.Column(db.String(12))
    reports = db.relationship('Report', backref='team', lazy='dynamic')

    def __repr__(self):
        return f'<Team {self.name}>'


@app.route('/')
def list_reports():
    sort = request.args.get('sort')
    if sort == 'downloads':
        reports = Report.query.order_by(Report.downloads.desc())
    else:
        reports = Report.query.order_by(Report.date.desc())

    print(sort)

    teams = Team.query.all()
    return render_template(
        'list_reports.html',
        reports=reports,
        teams=teams
    )


@app.route('/new', methods=['POST'])
def new_report():
    print(request.files)
    fields = ['username', 'title', 'ticker', 'team_id']
    r = Report(**{field: request.form[field] for field in fields})

    r.url = upload_file_to_s3(
        request.files['file'],
        secure_filename(f"{r.username} - {r.ticker} - {datetime.now().timestamp()}.pdf")
    )

    db.session.add(r)
    db.session.commit()

    return redirect(url_for('list_reports'))


if __name__ in '__main__':
    app.run()
