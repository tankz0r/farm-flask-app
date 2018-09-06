from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Denys'}
    posts = [
        {
            'author': 'Vova',
            'body': 'I am in Buffalo!'
        },
        {
            'author': 'Alex',
            'body': 'I am in Poland!'
        },
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
