"""users URL Configuration
"""
from django.urls import path, include,re_path
from . import views
#from django.contrib.auth.views import login（django1的版本）
from django.contrib.auth.views import LoginView#（django2的版本导入类）

LoginView.template_name = 'users/login.html'
app_name='users'
urlpatterns = [    
	#登录
    path('login/', LoginView.as_view(),
    	name='login'),    
    #注销
    re_path(r'^logout/$', views.logout_view, name='logout'),
    re_path(r'^register/$', views.register, name='register'),
]
