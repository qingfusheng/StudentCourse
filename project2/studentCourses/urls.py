"""定义studentCourses的URL模式"""
from django.conf.urls import url
from django.http import HttpResponse

from . import views

app_name = 'studentCourses'
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^mycourse/$', views.mycourse, name="mycourse"),
    url(r'^allcourse/$', views.allcourse, name='allcourse'),
    url(r'^my_course/$', views.helloParams),
    url(r'^xiaoli/$', views.xiaoli, name="xiaoli"),
    url(r'^zuoxi/$', views.zuoxi, name="zuoxi")
]
