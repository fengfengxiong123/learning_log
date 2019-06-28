"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include,re_path

from rest_framework import routers
from learning_logs import views

from django.views.generic import TemplateView

router = routers.DefaultRouter() #路由
router.register(r'article', views.ArticleViewSet) #路由地址与接口配置
router.register(r'artcontent', views.ArtContentViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('learning_logs.urls')),
    path('users/', include('users.urls')),

    #vue.js测试页面
    path('', TemplateView.as_view(template_name="index.html")),

    re_path(r'^api/', include(router.urls)), #包含进路由配置的url
    # re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
        #浏览器测试接口配置
    re_path(r'^tinymce/', include('tinymce.urls')), 
]
