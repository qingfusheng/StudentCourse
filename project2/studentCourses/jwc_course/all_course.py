# Created with Python AI
import json
import sqlite3

"""import requests
import json
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
    "Referer": "http://zhjwjs.scu.edu.cn/teacher/personalSenate/giveLessonInfo/thisSemesterClassSchedule/indexPublic",
}

data = {
    "zxjxjhh":"2021-2022-1-1",
    "kch":"",
    "kcm":"",
    "js":"",
    "kkxs":"",
    "skxq":"",
    "skjc":"",
    "xq":"",
    "jxl":"",
    "jas":"",
    "pageNum":"1",
    "pageSize":"10000",
    "kclb":""
}
print("正在从四川大学教务系统获取数据...")
session = requests.session()
res = session.post(url, headers=header, data=data)
text = res.text
print("获取数据成功")
j_text = json.loads(text)
courses = j_text["records"]
course = courses[0]"""
with open("course.json","r", encoding="utf-8") as f:
    courses_text = f.read()

courses = json.loads(courses_text)["list"]["records"]
print("连接数据库中")
try:
    conn = sqlite3.connect("../../db.sqlite3")
except Exception as error:
    print("数据库连接失败")
    quit()
print("数据库连接成功！")
print("正在清空表")
sql = "truncate table studentCourses_allcourse;"
conn.execute(sql)
conn.commit()
print("表清空成功")
print("正在向数据库写入数据")
i=1
for course in courses:
    print(course["id"], course["kch"], course["kxh"], course["kcm"], course["zxjxjhh"], course["skjs"], course["kkxsjc"], course["skzc"], course["skxq"], course["skjc"], course["cxjc"])
    sql = "insert into studentCourses_allcourse(course_id, kch, kxh, kcm, zxjxjhh, skjs, kkxy, classWeek, classDay, classSessions, continuingSession) values('%s','%s','%s','%s','%s','%s','%s','%s',%d, %d, %d )"%(course["id"], course["kch"], course["kxh"], course["kcm"], course["zxjxjhh"], course["skjs"], course["kkxsjc"], course["skzc"], course["skxq"], course["skjc"], course["cxjc"])
    conn.execute(sql)
    conn.commit()
    print(i)
    i+=1
conn.close()
print("写入数据成功")