#organization/adminx.py
#教育机构的adminx设置
import xadmin
from .models import CityDict,CourseOrg,Teacher

class CityDictAdmin(object):
    #城市名
    list_display = ['name','desc','add_time']
    search_fields = ['name','desc']
    list_filter = ['name','desc','add_time']

xadmin.site.register(CityDict,CityDictAdmin)


class CourseOrgAdmin(object):
    #教育机构
    list_display = ['name', 'desc', 'click_nums', 'fav_nums', 'add_time']
    search_fields = ['name', 'desc', 'click_nums', 'fav_nums']
    #有外键关系的要注意跨表查询
    list_filter = ['name', 'desc', 'click_nums', 'fav_nums', 'city__name', 'address', 'add_time']

xadmin.site.register(CourseOrg, CourseOrgAdmin)


class TeacherAdmin(object):

    list_display = ['name', 'org','work_company', 'add_time']
    #search_fields = ['org', 'name', 'work_company']
    #list_filter = ['org__name', 'name', 'work_company', 'click_nums', 'fav_nums', 'add_time']

xadmin.site.register(Teacher, TeacherAdmin)

