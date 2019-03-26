from django.db import models
from django.contrib.auth.models import AbstractUser

from datetime import datetime

#用户信息，admin无需注册
class UserProfile(AbstractUser):
    gender_choices = (
        ('male','男'),
        ('female','女')
    )

    nick_name = models.CharField('昵称',max_length=50,default='')#默认值default为空
    birthday = models.DateField('生日',null=True,blank=True)#允许为空
    gender = models.CharField('性别',max_length=10,choices=gender_choices,default='female')
    address = models.CharField('地址',max_length=100,default='')
    mobile = models.CharField('电话',max_length=11,null=True,blank=True)#允许为空
    image = models.ImageField(upload_to='image/%Y%m',default='image/default.png',max_length=100)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

#验证码类
class EmailVerifyRecord(models.Model):
    send_choice = (
        ('register','注册'),
        ('forget','找回密码')
    )

    code = models.CharField('验证码',max_length=20)
    email = models.EmailField('邮箱',max_length=50)
    send_type = models.CharField('发送类型',choices=send_choice,max_length=10)#现在注册还是找回密码
    send_time = models.DateTimeField('发送时间',default= datetime.now)

    class Meta:
        verbose_name= '邮箱验证码'
        verbose_name_plural = verbose_name


#轮播图
class Banner(models.Model):
    title = models.CharField('标题',max_length=100)
    image = models.ImageField('轮播图',upload_to='banner/%Y%m',max_length=100) #image上传到哪里
    url = models.URLField('访问地址',max_length=200)    # url是图片的路径
    index = models.IntegerField('播放顺序',default=100)     #index控制轮播图的播放顺序
    add_time = models.DateTimeField('添加时间',default=datetime.now)

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '轮播图:标题是:%s' %self.title     #在返回日志的时候很明了