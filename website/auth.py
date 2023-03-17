from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    #return render_template('login.html', text='Testing')
    return '<h1>LOGIN</h1>'

@ auth.route('/logout')
def logout():
    return '<p>Logout</p>'


@ auth.route('/sign-up')
def sign_up():
    #return render_template('sign_up.html')
    return '<h1>SIGN IN</h1>'