#coding:utf-8
import os
#基本配置
class Config():
    pass
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = ''
    FLASKY_MAIL_SENDER = 'FLASKY Admin <zhu-hero@qq.com>'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

#开发配置,集成基础配置
class DevelopConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI') or\
                              'sqlite:///%s' % (os.path.join(os.path.dirname(__file__), 'temp.db'))
    MAIL_SERVER = ''
    MAIL_PORT = ''
    MAIL_USE_TLS = ''
    MAIL_USE_SSL = ''
    MAIL_USENAME = ''
    MAIL_PASSWORD = ''


#生产配置
class ProductionConfig(Config):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess'


    pass


config={'dev':DevelopConfig,
        'product':ProductionConfig,
        }






