from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from studentCourses.jwc_course.get_xiaoli import get_xiaoli
from studentCourses.jwc_course.teacher_courses import search_teacher, get_X_teacher_info
from studentCourses.jwc_course.zuoxi_timeTable import get_zuoxi_time_table
from studentCourses.jwc_course.my_course import update_and_reset_database, get_my_courses
from studentCourses.weibo.hotSearch import get_html
from studentCourses.weibo.hotSearch import requests_news
from studentCourses.jwc_course.get_announcement_and_news import get_news_report, get_tonggao, get_yiqing_zhuanlan
import re


@login_required(login_url='/users/login')
def index(request):
    return render(request, 'studentCourses/index.html')


@login_required(login_url='/users/login')
def mycourse(request):
    # ret = update_and_reset_database()
    my_courses = get_my_courses()
    content = {"my_courses": my_courses}
    return render(request, 'studentCourses/mycourse.html', content)


@login_required(login_url='/users/login')
def allcourse(request):
    return render(request, 'studentCourses/allcourse.html')


def helloParams(request):
    p1 = request.GET.get('p1')
    p2 = request.GET.get('p2')
    if not p1 or not p2:
        return HttpResponse("错误的参数请求")
    return HttpResponse("p1 = " + p1 + "; p2 = " + p2)


@login_required(login_url='/users/login')
def xiaoli(request):
    content = {"images": get_xiaoli()}
    return render(request, 'studentCourses/xiaoli.html', content)


@login_required(login_url='/users/login')
def zuoxi(request):
    html_pre = '<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"/><title>本科生作息时间表</title><style type="text/css">body{background-color:pink;}</style></head><body><h3 class="page-title" align="center" style="font-size:50px">四川大学本科教学作息时间</h3>'
    html_aft = "</body></html>"
    info = get_zuoxi_time_table()
    html = html_pre + info + html_aft
    return HttpResponse(html)


@login_required(login_url='/users/login')
def hotSearch(request):
    html = get_html()
    return HttpResponse(html)


@login_required(login_url='/users/login')
def Teacher(request):
    if request.method == "POST" and request.POST:
        info = request.POST
        teacherName = info["teacherName"]
        search_result = search_teacher(info["departmentNum"], teacherName)
        content = {"search_result": search_result}

        # return HttpResponse(search_result)
        # print(content["search_result"])
        # return
        return render(request, "studentCourses/teacherResult.html", content)
    return render(request, "studentCourses/teacher.html")


def get_x_teacher(request):
    Num = request.GET.get("num")
    num_len = 0
    for i in Num:
        if i.isdigit():
            num_len += 1
    if num_len != len(Num):
        return HttpResponse("Wong params")
    content = get_X_teacher_info(Num)
    return HttpResponse(content)


@login_required(login_url='/users/login')
def Tonggao(request):
    tonggao = get_tonggao()
    return HttpResponse(tonggao)


@login_required(login_url='/users/login')
def News(request):
    news = get_news_report()
    return HttpResponse(news)


@login_required(login_url='/users/login')
def Yiqing(request):
    yiqing = get_yiqing_zhuanlan()
    return HttpResponse(yiqing)
