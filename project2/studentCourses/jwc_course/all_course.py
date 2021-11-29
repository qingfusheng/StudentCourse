import sqlite3
import requests
import json

url = "http://zhjwjs.scu.edu.cn/teacher/personalSenate/giveLessonInfo/thisSemesterClassSchedule/getCourseArragementPublic"


def get_all_course():
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
        "zxjxjhh": "2021-2022-1-1",
        "kch": "",
        "kcm": "",
        "js": "",
        "kkxs": "",
        "skxq": "",
        "skjc": "",
        "xq": "",
        "jxl": "",
        "jas": "",
        "pageNum": "1",
        "pageSize": "30",
        "kclb": ""
    }

    print("正在从四川大学教务系统获取数据...")
    session = requests.session()
    res = session.post(url, headers=header, data=data)
    courses_text = res.text
    print("获取数据成功")
    return json.loads(courses_text)


def write_to_sql():
    j_content = get_all_course()
    courses = j_content["list"]["records"]
    print("连接数据库中")
    try:
        conn = sqlite3.connect("../../db.sqlite3")
    except Exception as error:
        print("数据库连接失败")
        quit()
    print("数据库连接成功！")
    while True:
        ret = input("是否重置数据库(Y/N)")
        print(ret)
        if ret == 'N':
            print("停止清空表")
        elif ret == 'Y':
            print("正在清空表")
            quit()
        else:
            print("输入有误，请重新输入")
            continue
    sql = "delete from studentCourses_allcourse"
    sql2 = "update sqlite_sequence SET seq=0 where name=\"studentCourses_allcourse\""
    conn.execute(sql)
    conn.execute(sql2)
    conn.commit()
    print("表清空成功")
    print("正在向数据库写入数据")
    i = 1
    for course in courses:
        print(i, course["id"], course["kch"], course["kxh"], course["kcm"], course["zxjxjhh"], course["skjs"],
              course["kkxsjc"], course["skzc"], course["skxq"], course["skjc"], course["cxjc"])
        if course["skxq"] is None:
            course["skxq"] = 0
        if course["skjc"] is None:
            course["skjc"] = 0
        if course["cxjc"] is None:
            course["cxjc"] = 0
        sql = "insert into studentCourses_allcourse(course_id, kch, kxh, kcm, zxjxjhh, skjs, kkxy, classWeek, classDay, classSessions, continuingSession) values('%s','%s','%s','%s','%s','%s','%s','%s',%d, %d, %d )" % (
            course["id"], course["kch"], course["kxh"], course["kcm"], course["zxjxjhh"], course["skjs"],
            course["kkxsjc"],
            course["skzc"], course["skxq"], course["skjc"], course["cxjc"])
        try:
            conn.execute(sql)
            conn.commit()
        except Exception as error:
            print("!!!Error")
            print(i, course["id"], course["kch"], course["kxh"], course["kcm"], course["zxjxjhh"], course["skjs"],
                  course["kkxsjc"], course["skzc"], course["skxq"], course["skjc"], course["cxjc"])
        i += 1
    conn.close()
    print("写入数据成功")


write_to_sql()
