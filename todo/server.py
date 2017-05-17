from flask import Flask, url_for, render_template, jsonify, request, make_response
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from config import Base

server = Flask(__name__)
server.config.from_object(Base)


""" Flask Forms"""
class HelloForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])


class TodoForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])

""" End Flask Forms """

@server.route('/')
def index():
    """
    Render index.html file

    :return: obj - renders index page
    """
    return render_template('index.html')


@server.route('/sayhi', methods=['GET', 'POST'])
def say_hi():
    form = HelloForm()
    name = 'Guest'
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('hello.html', name=name, form=form)


def run_server():
    server.run(host='127.0.0.1', port=8088, threaded=True)

if __name__ == '__main__':
    run_server()
