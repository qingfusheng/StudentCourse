"""定义studentCourses的URL模式"""
from django.conf.urls import url
from django.http import HttpResponse

from . import views

app_name = 'studentCourses'
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^mycourse/$', views.mycourse, name="mycourse"),
    url(r'^allcourse/$', views.allcourse, name='allcourse'),
    url(r'^hello/$', views.helloParams),
    url(r'^xiaoli/$', views.xiaoli, name="xiaoli"),
    url(r'^zuoxi/$', views.zuoxi, name="zuoxi"),
    url(r'^hotsearch/$', views.hotSearch, name="hotSearch"),
    url(r'^teacher/$', views.Teacher, name="Teacher"),
    url(r'^teacherNum/$', views.get_x_teacher, name='get_x_teacher'),
    url(r'^tonggao/$', views.Tonggao, name="Tonggao"),
    url(r'^news/$', views.News, name="News"),
    url(r'^yiqing/$', views.Yiqing, name="Yiqing"),
    url(r'^freeroom/$', views.free_room, name="free_room"),
]
