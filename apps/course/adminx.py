#course/adminx.py
#课程
import xadmin

from .models import Course,CourseResourse,Lesson,Video
#从models中导入课程，课程资源，章节，视频类
class CourseAdmin(object):
    #课程
    #显示的元素
    list_display = ['name','desc','detail','degree','learn_time','students']
    #搜索
    search_fields = ['name','desc','degree','students']
    #过滤
    list_filter = ['name','desc','detail','degree','learn_time','students','add_time']

xadmin.site.register(Course,CourseAdmin)

class CourseResourseAdmin(object):
    #课程资源，与课程有关
    list_display = ['course','name','add_time']

    search_fields = ['course','name']
#课程资源，按课程名过滤，跨表查找要__
    list_filter = ['course__name','name','add_time']

xadmin.site.register(CourseResourse,CourseResourseAdmin)

class LessonAdmin(object):
    #章节，与课程有关
    list_display = ['course','name','add_time']

    search_fields = ['course','name']
    list_filter = ['course','name','add_time']

xadmin.site.register(Lesson,LessonAdmin)

class VideoAdmin(object):
    #视频，与章节有关
    list_display = ['lesson','name','add_time']
    search_fields = ['lesson','name']
    list_filter = ['lesson','name','add_time']

xadmin.site.register(Video,VideoAdmin)