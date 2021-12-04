from django.conf.urls import url
from django.contrib.auth.views import LoginView
from . import views

app_name ='users'
urlpatterns = [
    # 登录页面
    url(r'^login/$', views.login_view, name='login_view'),
    url(r'^logout/$', views.logout_view, name="logout_view")
]

