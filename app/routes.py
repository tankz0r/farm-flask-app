from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.user_name.data, form.keep_logged.data))
        return redirect('/index')
    return render_template('login.html', title='login', form=form)
