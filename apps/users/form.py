# users/forms.py

from django import forms
from captcha.fields import CaptchaField # 导入验证码包

# 登录表单验证
class LoginForm(forms.Form):
    # 用户名密码不能为空
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=3)


#注册验证表单,
class RegistForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,min_length=5) #不能为空，不能少于5个

    #验证码
    captcha = CaptchaField(error_messages={'invalid': '验证码错误'})