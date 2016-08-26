#coding:utf-8
"""
启动文件,从这里启动APP
"""
from app import create_app,db
from flask_migrate import Migrate,MigrateCommand
from flask_script import Shell,Manager
from app.excel import Post,Category

#传入开发配置
app = create_app('dev')
#初始化脚本扩展
manager = Manager(app)
#数据库迁移,传入app实例,数据库实例
migrate = Migrate(app,db)

#注册实例,方便在shell中调用
def make_shell_context():
    return dict(app=app,db=db,Post=Post,Category=Category)

manager.add_command("shell",Shell(make_context=make_shell_context))
manager.add_command("db",MigrateCommand)

if __name__ == '__main__':
    manager.run()