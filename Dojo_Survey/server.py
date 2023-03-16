# Steps to create a flask app
# 1. pip install pipenv (follow the screenshot image)
# 2.
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secretpassword"


@app.route('/')
def index():
     return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
     session['name'] = request.form['name']
     session['location'] = request.form['location']
     session['language'] = request.form['language']
     session['comment'] = request.form['comment']

     return redirect('/result')


@app.route('/result')
def result():
     name = session.get('name')
     location = session.get('location')
     language = session.get('language')
     comment = session.get('comment')

     return render_template('result.html', name=name, location=location, language=language, comment=comment)


@app.route('/goback')
def go_back():
     return redirect('/')









if __name__ == "__main__":
     app.run( debug = True, port=5001 )