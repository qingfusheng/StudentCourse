import requests
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from studentCourses.jwc_course.get_xiaoli import get_xiaoli
from studentCourses.jwc_course.teacher_courses import search_teacher, get_X_teacher_info
from studentCourses.jwc_course.zuoxi_timeTable import get_zuoxi_time_table
from studentCourses.jwc_course.my_course import update_and_reset_database, get_my_courses
from studentCourses.weibo.hotSearch import get_html, requests_news
from studentCourses.jwc_course.get_announcement_and_news import get_news_report, get_tonggao, get_yiqing_zhuanlan
from studentCourses.jwc_course.free_classroom import find_free_classroom
from users.storage.user_config import read_config
import re


@login_required(login_url='/users/login')
def index(request):
    personal_info = read_config()
    tonggao = get_tonggao()
    print("Tonggao success")
    news = get_news_report()
    print("news success")
    yiqing = get_yiqing_zhuanlan()
    print("yiqing success")
    hotSearch = requests_news()
    print("hotSearch Success")
    content = {
        "personal_info": personal_info,
        "tonggao": tonggao,
        "news": news,
        "yiqing": yiqing,
        "hotSearch": hotSearch[0:30]
    }
    return render(request, 'studentCourses/index.html', content)


@login_required(login_url='/users/login')
def mycourse(request):
    # ret = update_and_reset_database()
    my_courses = get_my_courses()
    content = {"my_courses": my_courses}
    #  return HttpResponse(my_courses)
    return render(request, 'studentCourses/mycourse.html', content)


@login_required(login_url='/users/login')
def allcourse(request):
    if request.method == "POST" and request.POST:
        info = request.POST
        print(info)
        url = "http://zhjwjs.scu.edu.cn/teacher/personalSenate/giveLessonInfo/thisSemesterClassSchedule/getCourseArragementPublic"
        header = {
            "Host": "zhjwjs.scu.edu.cn",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "Accept-Language": "zh-CN,zh-Hans;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "http://zhjwjs.scu.edu.cn",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15",
            "Connection": "keep-alive",
            # "Referer": "http://zhjwjs.scu.edu.cn/teacher/personalSenate/giveLessonInfo/thisSemesterClassSchedule/indexPublic",
        }
        data = {
            "zxjxjhh": info["zxjxjhh"],
            "kch": info["kch"],
            "kcm": info["kcm"] ,
            "js": info["js"],
            "kkxs": info["kkxs"],
            "skxq": info["skxq"],
            "skjc": info["skjc"],
            "xq": info["xq"],
            "jxl": info["jxl"],
            "jas": info["jas"],
            "pageNum": '1',
            "pageSize": '10000',
            "kclb": '',
        }
        print(data)
        print("正在从四川大学教务系统获取数据...")
        session = requests.session()
        res = session.post(url, headers=header, data=data)
        course_result = res.json()
        content = {"course_result":course_result["list"]["records"]}
        return render(request, 'studentCourses/allcourse.html', content)
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
    html_pre = '<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"/><title>本科生作息时间表</title><style type="text/css">body{background-color:white;}</style></head><body><h3 class="page-title" align="center" style="font-size:50px">四川大学本科教学作息时间</h3>'
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
        print("Searching begin")
        search_result = search_teacher(info["departmentNum"], teacherName)
        print("result gotten")
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
    courses = get_X_teacher_info(Num)[0]
    print(type(courses))
    print(courses)
    content = {"courses": courses}
    return render(request, "studentCourses/teacherCourse.html", content)


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


# @login_required(login_url='/users/login')
def free_room(request):
    room_info = find_free_classroom()
    return HttpResponse(room_info["data"]["roomdata"])
