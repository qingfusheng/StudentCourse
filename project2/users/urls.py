from django.conf.urls import url
from django.contrib.auth.views import LoginView
from . import views

app_name ='users'
urlpatterns = [
    # 登录页面
    url(r'^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),
    url(r'^login2/$', views.login2, name='login2'),
]

