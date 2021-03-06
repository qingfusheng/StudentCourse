import requests

from users.storage.user_config import read_config
from studentCourses.jwc_course.login import get_session

header = {
    "Host": "zhjw.scu.edu.cn",
    "Connection": "keep-alive",
    "Content-Length": "92",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "http://zhjw.scu.edu.cn",
    "Referer": "http://zhjw.scu.edu.cn/student/teachingResources/teacherCurriculum/index",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7"
}


"""def my_login():
    info = read_config()
    ret, session = check_valid(info["username"], info["password"])
    return ret, session"""


def search_teacher(departmentNum="", teacherName=""):
    print("Getting Session")
    session = get_session()
    print("Session success")
    search_teacher_url = "http://zhjw.scu.edu.cn/student/teachingResources/teacherCurriculum/search"
    search_data = {
        "executiveEducationPlanNumber": "2021-2022-1-1",
        "departmentNum": departmentNum,
        "teacherName": teacherName,
        "pageNum": "1",
        "pageSize": "10000"
    }
    print("Begin send")
    res = session.post(search_teacher_url, data=search_data, headers=header)
    j_text = res.json()
    print("receive successfully")
    teacher_list = []
    for each in j_text[0]["records"]:
        name = each["teacherName"]
        department = each["departmentName"]
        teacherNumber = each["id"]["teacherNumber"]
        sex = each["sex"]
        teacher_list.append((teacherNumber, name, sex, department))
    print("The length of teacher search result:",len(teacher_list))
    return teacher_list


def get_X_teacher_info(teacherNumber):
    session = get_session()
    X_teacher_url = "http://zhjw.scu.edu.cn/student/teachingResources/teacherCurriculum/searchCurriculumInfo/callback?planCode=2021-2022-1-1&teacherNum=" + teacherNumber
    res = session.get(X_teacher_url)
    j_text = res.json()
    return j_text