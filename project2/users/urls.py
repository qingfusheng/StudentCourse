from django.conf.urls import url
from django.contrib.auth.views import LoginView
from . import views

app_name ='users'
urlpatterns = [
    # 登录页面
    url(r'^login/$', views.login, name='login'),
]

