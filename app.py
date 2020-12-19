from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title='Report Submission')


if __name__ in '__main__':
    app.run(DEBUG=True)
