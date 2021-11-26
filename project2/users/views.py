import time

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from studentCourses.jwc_course.login import check_valid
import requests


# Create your views here.
def login(request):
    """"""
    if request.method == "POST" and request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        ret = check_valid(username, password)
        if ret == 1:
            response = HttpResponseRedirect('/')
            response.set_cookie("username", username)
            return response

        elif ret == 0:
            messages.error(request, "用户或密码不正确")
            return render(request, 'users/login.html')
        elif ret == -1:
            messages.error(request, "教务管理系统不可达,请稍后重试")
            return render(request, 'users/login.html')
    return render(request, 'users/login.html')
