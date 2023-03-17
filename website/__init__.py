from flask import Flask


def create_app():
    app= Flask(__name__) #__name__ the name of the file
    app.config['SECRET_KEY'] = 'Hello'#To encrypt cookies and secure data of our website

    # We have to register our blueprints
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/') #Urlprefix if we want to add a prefix to the url to access the blueprints inside

    return app

