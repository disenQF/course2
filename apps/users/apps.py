from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    verbose_name = '用户'

#给用户设置别名后还要在__init__.py中设置
#default_app_config = 'users.apps.UsersConfig'