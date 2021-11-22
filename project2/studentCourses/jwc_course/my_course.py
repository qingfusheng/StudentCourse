# -*- coding: UTF-8 -*-
import json
import time
import sqlite3
import requests

my_url = "http://my.scu.edu.cn/userPasswordValidate.portal"
captcha_url = "http://zhjw.scu.edu.cn/img/captcha.jpg"  # 验证码地址
index_url = "http://zhjw.scu.edu.cn/index.jsp"
login_url = "http://zhjw.scu.edu.cn/j_spring_security_check"  # 登录接口
already_select_course_url = "http://zhjw.scu.edu.cn/student/courseSelect/thisSemesterCurriculum/callback"  # 已选课程查询地址
header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Host': 'zhjw.scu.edu.cn',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3782.0 Safari/537.36 Edg/76.0.152.0'
}

my_header = {
    "Host": "my.scu.edu.cn",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "160",
    "Origin": "http://my.scu.edu.cn",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}

j_username = input("Username:")
j_password = input("password:")
print(j_username)
print(j_password)


def login1(session):
    try:
        print("username:", j_username)
        print("Logining...")
        data = {
            "Login.Token1": j_username,
            "Login.Token2": j_password,
            "goto": "http://my.scu.edu.cn/loginSuccess.portal",
            "gotoOnFail": "http://my.scu.edu.cn/LoginFailure.portal"
        }
        response = session.post(my_url, headers=my_header, data=data)
        response = session.get(index_url, headers=header)
        data = {
            "j_username": j_username,
            "j_password": "1",
            "j_captcha": ""
        }
        response = session.post(login_url, headers=header, data=data)
        html = response.text
        if "四川大学教务管理系统" in html:
            print("登陆成功")
            return "success"
        else:
            return None
    except requests.exceptions or BaseException as error:
        print(error)
        return None

def write_info_to_database(courses_text):
    with open("my_course.json", "r", encoding="utf-8") as f:
        courses_text = f.read()

    courses = json.loads(courses_text)["xkxx"][0]
    print("连接数据库中")
    try:
        conn = sqlite3.connect("../../db.sqlite3")
    except Exception as error:
        print("数据库连接失败")
        quit()
    print("数据库连接成功！")
    print("正在清空表")
    sql = "delete from studentCourses_mycourse"
    sql2 = "update sqlite_sequence SET seq=0 where name='studentCourses_mycourse'"
    conn.execute(sql)
    conn.execute(sql2)
    conn.commit()
    print("表清空成功")
    print("正在向数据库写入数据")
    i = 1
    temps = [i for i in courses]
    for temp in temps:
        course = courses[temp]
        # print(i, course["timeAndPlaceList"][0]["id"], course["id"]["coureNumber"], course["id"]["coureSequenceNumber"], course["courseName"], course["id"]["executiveEducationPlanNumber"], course["attendClassTeacher"],  course["timeAndPlaceList"][0]["classWeek"], course["timeAndPlaceList"][0]["classDay"], course["timeAndPlaceList"][0]["classSessions"], course["timeAndPlaceList"][0]["continuingSession"])
        course["timeAndPlaceList"]
        if course["timeAndPlaceList"] == []:
            course["timeAndPlaceList"].append({
                "classDay": 0,
                "classSessions": 0,
                "classWeek": "",
                "continuingSession": 0,
                "id": ""
            })
        sql = "insert into studentCourses_mycourse(course_id, kch, kxh, kcm, zxjxjhh, skjs, classWeek, classDay, classSessions, continuingSession) values('%s','%s','%s','%s','%s','%s','%s',%d, %d, %d )" % (
        course["timeAndPlaceList"][0]["id"], course["id"]["coureNumber"], course["id"]["coureSequenceNumber"],
        course["courseName"], course["id"]["executiveEducationPlanNumber"], course["attendClassTeacher"],
        course["timeAndPlaceList"][0]["classWeek"], course["timeAndPlaceList"][0]["classDay"],
        course["timeAndPlaceList"][0]["classSessions"], course["timeAndPlaceList"][0]["continuingSession"])
        print(i)
        try:
            conn.execute(sql)
            conn.commit()
        except Exception as error:
            print(error)
        i += 1
    print("end")
    conn.close()
    print("写入数据成功")


if __name__ == "__main__":
    session = requests.session()
    while True:
        loginResponse = login1(session)
        if loginResponse == "success":
            break
        else:
            print("登陆失败！")
            time.sleep(2)
    my_course = json.loads(session.get(url=already_select_course_url, headers=header).text)
    write_info_to_database(my_course)
