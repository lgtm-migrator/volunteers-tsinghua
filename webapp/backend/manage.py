# -*- coding: utf-8 -*-
'''测试阶段-启动文件'''
import os
import sys

from flask_script import Manager, Shell
from flask_migrate import Migrate,MigrateCommand
from werkzeug.routing import EndpointPrefix

from app import create_app,db
from app.model import User


def make_shell_context():
    return dict(app=app, db=db, User=User)

def init_admin(app):
    '''初始化管理员用户'''

    with app.test_request_context():
        from .app.model import AdminUser

        db = app.db
        default_email = 'volunteers@tsinghua.edu.cn'
        default_name = 'spb17'
        default_password = 'admin'

        if AdminUser.query.filter_by(email=default_email).count() < 1:
            user_obj = AdminUser()
            user_obj.name = default_name
            user_obj.email = default_email
            user_obj.password = default_password
            db.session.add(user_obj)
            db.session.commit()
        # else:
        #     user_obj = AdminUser.query.first().to_dict()
        # if isinstance(user_obj, AdminUser):
        #     print(user_obj)


proj_root = os.path.abspath(os.path.dirname(__file__))
os.environ['PROJ_ROOT'] = proj_root
app = create_app()
app.proj_root = proj_root
manager = Manager(app)
migrate=Migrate(app,db)
manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()