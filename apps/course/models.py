from datetime import datetime

from django.db import models

#课程->章节->章节内的视频->课程资源
class Course(models.Model):  #课程表
    DEGREE_CHOICES = (
        ('cj','初级'),
        ('zj','中级'),
        ('gj','高级')
    )
    name = models.CharField('课程名',max_length=50)
    desc = models.CharField('课程描述',max_length=300)
    detail = models.TextField('课程详情')
    degree = models.CharField('难度',choices=DEGREE_CHOICES,max_length=5)
    learn_time = models.IntegerField('学习时长(分钟)',default=0)
    students = models.IntegerField('学习人数',default=0)
    fav_nums = models.IntegerField('收藏人数',default=0)
    image = models.ImageField('封面图',upload_to='courses/%Y/%m',max_length=100)
    click_num = models.IntegerField('点击数',default=0)
    add_time = models.DateTimeField('添加时间',default=datetime.now)

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Lesson(models.Model):#章节信息表
    course = models.ForeignKey(Course,verbose_name='课程',on_delete=models.CASCADE)#一对多外键关联，
    name = models.CharField('章节名',max_length=100)
    add_time = models.DateTimeField('添加时间',default=datetime.now)

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '《{0}》课程的章节>>{1}'.format(self.course,self.name)
        #format是字符串处理函数

class Video(models.Model): #章节视频表
    lesson = models.ForeignKey(Lesson,verbose_name='章节',on_delete=models.CASCADE)
    name = models.CharField('视频名',max_length=100)
    add_time = models.DateTimeField('添加时间',default=datetime.now)

    class Meta:
        verbose_name ='视频'
        verbose_name_plural = verbose_name

class CourseResourse(models.Model):  #课程资源表
    course = models.ForeignKey(Course,verbose_name='课程',on_delete=models.CASCADE)
    name = models.CharField('资源名',max_length=100)
    download = models.FileField('资源文件',upload_to='course/resourse/%Y/%m',max_length=100)
    add_time = models.DateTimeField('添加时间',default=datetime.now)

    class Meta:
        verbose_name = '课程资源'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '《{0}》课程的资源文件>>{1}'.format(self.course,self.name)
        #format是字符串处理函数


