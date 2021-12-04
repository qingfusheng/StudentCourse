import time
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse
from studentCourses.jwc_course.login import check_valid
from django.contrib.auth import logout, login, authenticate
import requests


# Create your views here.
def login_view(request):
    """"""
    href = request.GET.get("next")
    print("href", href)
    if request.method == "POST" and request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        rtt = check_valid(username, password)
        ret = rtt[0]
        if ret == 1:
            authenticated_user = authenticate(username="private_user", password="cxd2564526674")
            login(request, authenticated_user)
            """response = HttpResponse("LoginSuccess")
            response.set_cookie("username", username)
            return response"""
            if href:
                response = HttpResponseRedirect(href)
            else:
                response = HttpResponseRedirect("/")
            return response

        elif ret == 0:
            messages.error(request, "用户或密码不正确")
            return render(request, 'users/login.html')
        elif ret == -1:
            messages.error(request, "教务管理系统不可达,请稍后重试")
            return render(request, 'users/login.html')
    return render(request, 'users/login.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/users/login')
