# adminx和admin功能相似，要新建adminx
#users/adminx.py
import xadmin

#xadmin配置,只需一个app中配置就行
from xadmin import views

from .models import EmailVerifyRecord,Banner

#注册验证码类
#xadmin 与admin不同处，admin是继承admin,而xadmin是继承object
class EmailVerifyRecordAdmin(object):
    #显示的列
    list_display = ['code','email','send_type','send_time']
    #搜索的字段
    search_fields = ['code','email','send_type']
    #过滤
    list_filter = ['code', 'email','send_type','send_time']

xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)

#注册轮播图
class BannerAdmin(object):
    #显示的列
    list_display = ['title','image','url','index','add_time']
    #搜索的字段
    search_fields = ['title','url','index']
    #过滤
    list_filter = ['title','image','url','index','add_time']

xadmin.site.register(Banner,BannerAdmin)


#xadmin配置
class BaseSetting(object):
    #开启主题
    enable_themes = True
    use_bootswatch =True

xadmin.site.register(views.BaseAdminView,BaseSetting)

# 全局修改，固定写法
class GlobalSettings(object):
    # 修改title
    site_title = '在线教育平台'
    # 修改footer
    site_footer = '爱笑的大学生'
    # 收起菜单
    menu_style = 'accordion'

# 将title和footer信息进行注册
xadmin.site.register(views.CommAdminView,GlobalSettings)