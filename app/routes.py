from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Chris'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    # The form.validate_on_submit() method does all the form processing work. When the 
    # browser sends the GET request to receive the web page with the form, this method 
    # is going to return False, so in that case the function skips the if statement and 
    # goes directly to render the template in the last line of the function.
    
    # login information submitted (POST)
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))

    # no login information submitted (GET)
    return render_template('login.html', title='Sign In', form=form)