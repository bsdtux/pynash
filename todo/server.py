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

@server.route('/slide2')
def slide2():
    """
    Render the slide2.html file

    :return: obj - renders slide 2 
    """
    return render_template('slide2.html')

@server.route('/slide3')
def slide3():
    """
    Render the slide3.html file

    :return: obj - renders slide 3 
    """
    return render_template('slide3.html')

@server.route('/slide4')
def slide4():
    """
    Render the slide4.html file

    :return: obj - renders slide 4
    """
    return render_template('slide4.html')

@server.route('/slide5')
def slide5():
    """
    Render the slide5.html file

    :return: obj - renders slide 5
    """
    return render_template('slide5.html')

@server.route('/slide6')
def slide6():
    """
    Render the slide6.html file

    :return: obj - renders slide 6
    """
    return render_template('slide6.html')

def run_server():
    server.run(host='127.0.0.1', port=8088, threaded=True)

if __name__ == '__main__':
    run_server()
