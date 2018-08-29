# coding=utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# from config import config
from config import config
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    db.app = app

    # 注册蓝本

    from .main import main as main_blueprint
    from .main.test_blueprint import test1 as t
    app.register_blueprint(main_blueprint)
    app.register_blueprint(t,url_prefix='/test')

    from .main.upload_BP import upload as upload
    app.register_blueprint(upload,url_prefix='/upload')

    from .main.DataBase_Select_BP import DB_Sel as db_sel
    app.register_blueprint(db_sel,url_prefix='/db_sel')



    return app