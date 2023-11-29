from flask import Flask, render_template
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config
from .main import backgroundfunction

moment = Moment()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    moment.init_app(app)
    app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///test.db'
    with app.app_context():
        db.init_app(app)
        app.config['back_func'] = backgroundfunction.checkFlight()

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)


    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app