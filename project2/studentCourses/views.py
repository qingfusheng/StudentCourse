from django.http import HttpResponse
from django.shortcuts import render
from studentCourses.jwc_course.get_xiaoli import get_xiaoli
from studentCourses.jwc_course.zuoxi_timeTable import get_zuoxi_time_table
from studentCourses.jwc_course.my_course import update_and_reset_database, get_my_courses


# Create your views here.
def index(request):
    return render(request, 'studentCourses/index.html')


def mycourse(request):
    # ret = update_and_reset_database()
    my_courses = get_my_courses()
    content = {"my_courses": my_courses}
    return render(request, 'studentCourses/mycourse.html', content)


def allcourse(request):
    return render(request, 'studentCourses/allcourse.html')


def helloParams(request):
    p1 = request.GET.get('p1')
    p2 = request.GET.get('p2')
    if not p1 or not p2:
        return HttpResponse("错误的参数请求")
    return HttpResponse("p1 = " + p1 + "; p2 = " + p2)


def xiaoli(request):
    content = {"images": get_xiaoli()}
    return render(request, 'studentCourses/xiaoli.html', content)

def zuoxi(request):
    html_pre = '<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"/><title>本科生作息时间表</title><style type="text/css">body{background-color:pink;}</style></head><body><h3 class="page-title" align="center" style="font-size:50px">四川大学本科教学作息时间</h3>'
    html_aft = "</body></html>"
    info = get_zuoxi_time_table()
    html = html_pre+info+html_aft
    return HttpResponse(html)