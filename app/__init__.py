#coding:utf-8
"""
程序包的作用,把资源集中到这里,方便导入
1、需要通过app初始化的扩展

"""
from flask import Flask
from flask_bootstrap import Bootstrap #bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_script import Manager
from flask_mail import Mail
from flask_moment import Moment
from config import config
#后续集中传入flask实例完成初始化
bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()
moment = Moment()

#工厂函数,传入配置,返回app实例
def create_app(config_name):
    #初始化
    app = Flask(__name__)
    #通过配置词典导入配置
    app.config.from_object(config[config_name])

    #通过init_app方法完成扩展的初始化
    bootstrap.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    moment.init_app(app)

    #注册蓝本
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .excel import excel as excel_blueprint
    app.register_blueprint(excel_blueprint,url_prefix='/excel')
    return app

