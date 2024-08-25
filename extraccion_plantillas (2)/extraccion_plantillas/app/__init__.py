from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import the routes
    from .routes import app as routes_app
    app.register_blueprint(routes_app)

    return app
