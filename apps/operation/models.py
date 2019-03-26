from datetime import datetime
from django.db import models
from users.models import UserProfile
from course.models import Course

#UseAsk 用户咨询
#UserMessage  用户消息表
#CourseComments 用户评论
#UserCourse 用户学习的课程
#UserFavorite 用户收藏
class UserAsk(models.Model):
    name =models.CharField('姓名',max_length=20)
    mobile = models.CharField('手机',max_length=11)
    course_name = models.CharField('课程名称',max_length=50)
    add_time = models.DateTimeField('添加时间',default=datetime.now)

    class Meta:
        verbose_name = '用户咨询'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class UserMessage(models.Model):    #用户消息
    user =models.IntegerField('接受用户',default=0) #user字段，默认0代表消息是发给所有用户，而不是某个单独的用户；可以通过user.id发给特定用户消息
    message = models.CharField('消息内容',max_length=500)
    has_read = models.BooleanField('是否已读',default=False)
    add_time = models.DateTimeField('添加时间',default=datetime.now)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

class CourseComments(models.Model):     #课程评论
    user = models.ForeignKey(UserProfile,verbose_name='用户',on_delete=models.CASCADE)
    course = models.ForeignKey(Course,verbose_name='课程',on_delete=models.CASCADE)
    comments = models.CharField('评论',max_length=200)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '课程评论'
        verbose_name_plural = verbose_name


class UserCourse(models.Model):     #用户学习的课程
    user = models.ForeignKey(UserProfile,verbose_name='用户',on_delete=models.CASCADE)
    course = models.ForeignKey(Course,verbose_name='课程',on_delete=models.CASCADE)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '用户课程'
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):       #用户收藏（课程，教育机构，老师）
    FAV_TYPE =(
        (1,'课程'),
        (2,'课程机构'),
        (3,'老师')
    )

    user = models.ForeignKey(UserProfile, verbose_name='用户', on_delete=models.CASCADE)
    fav_id = models.IntegerField('数据id', default=0)
    fav_type = models.IntegerField(verbose_name='收藏类型', choices=FAV_TYPE, default=1)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name
