from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Marinos'}
    posts = [
        {
            'author': {'username': 'Bob'},
            'body': 'Beautiful day in Thessaloniki!'
        },
        {
            'author': {'username': 'Alice'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)