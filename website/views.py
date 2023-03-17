from flask import Blueprint, render_template

#Blueprint = urls, routes so we can split our views

views = Blueprint('views', __name__)

@views.route('/') # Decorator. To define the view route
def home(): # When you hit the route will run the function
    # return render_template('home.html')
    return '<h1>Home PAGE</h1>'