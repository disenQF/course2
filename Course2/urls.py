import xadmin
from django.urls import path, include, re_path
# 引用通用模板
from django.views import generic
from apps.users.views import LoginView, RegisterView, ActiveUserView  # 基于类的url

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('', generic.TemplateView.as_view(template_name='index.html'), name='index'),
    path('login/', LoginView.as_view(), name='login'),  # 用户登录路由
    path('register/', RegisterView.as_view(), name='register'),
    path('captcha/', include('captcha.urls')),
    re_path('active/(?P<active_code>.*)/', ActiveUserView.as_view(), name='user_active'),  # 激活用户的url
]
