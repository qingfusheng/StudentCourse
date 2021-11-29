
from django.conf.urls import url
from django.http import HttpResponse

from . import views

app_name = 'studentCourses'
urlpatterns = [
    url(r'^$', views.getContent, name="getContent"),
]
