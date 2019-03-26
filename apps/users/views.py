from django.http import HttpResponse
from django.shortcuts import render, redirect
# 导入，登入，和用户认证模块
from django.contrib.auth import login, authenticate

# 邮箱登录
from django.contrib.auth.backends import ModelBackend  # 继承ModelBackend类
from django.views.generic.base import View
from django.db.models import Q
from .form import LoginForm, RegistForm

# 口令 加密
from django.contrib.auth.hashers import make_password

# 发送邮件
from utils.email_send import send_register_eamil
from users.models import UserProfile, EmailVerifyRecord


# 用户登录方法
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        # 实例化
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # 获取用户提交的用户名和密码
            user_name = request.POST.get('username', None)
            pass_word = request.POST.get('password', None)
            # 成功返回user对象,失败None
            user = authenticate(username=user_name, password=pass_word)
            # 如果不是null说明验证成功
            if user is not None:
                login(request, user)
                return render(request, 'index.html')
            # 只有当用户名或密码不存在时，才返回错误信息到前端
            else:
                return render(request, 'login.html', {'msg': '用户名或密码错误', 'login_form': login_form})

        else:
            return render(request, 'login.html', {'login_form': login_form})


# 增加邮箱登录
# 用户名和邮箱都可登录
class CustomBackend(ModelBackend):
    def authenticate(self, request,
                     username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))

            if user.check_password(password):
                return user
        except Exception as e:
            return None


# 注册,登录注册都是用的类
class RegisterView(View):

    '''用户注册'''
    def get(self, requset):
        return render(requset, 'register.html')

    def post(self, request):
        register_form = RegistForm(request.POST)
        if register_form.is_valid():
            email = register_form.cleaned_data.get('email')
            password = register_form.cleaned_data.get('password')
            user = UserProfile(email=email,
                               password=make_password(password))
            user.is_active = False
            user.is_staff = False

            user.save()

            send_register_eamil(email)

            html = "<h3>注册成功</h3>" \
                   "<script>" \
                   "setTimeout(function(){ window.open('/login/')}, 3000);" \
                   "</script>"

            return HttpResponse(html)

        return render(request, 'register.html', locals())


class ActiveUserView(View):
    '''用户激活函数'''
    def get(self, request, active_code):
        html = """
        <h3>用户激活</h3>
        <h4> 点击跳转到主页</h4>
        """
        return HttpResponse(html, 'text/html;charset=utf-8', 200)
