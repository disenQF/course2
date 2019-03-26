from django.apps import AppConfig


class CourseConfig(AppConfig):
    name = 'course'
    verbose_name = '课表'

#给用户设置别名后还要在__init__.py中设置
#default_app_config = 'app名.apps.app名（大写首字母）Config'