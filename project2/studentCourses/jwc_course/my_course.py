# -*- coding: UTF-8 -*-
import ast
import json
import random
import re
import time

import muggle_ocr
import requests
from PIL import Image
import hashlib

my_url = "http://my.scu.edu.cn/userPasswordValidate.portal"
captcha_url = "http://zhjw.scu.edu.cn/img/captcha.jpg"  # 验证码地址
index_url = "http://zhjw.scu.edu.cn/"  # 主页地址
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
    #    "Referer": "http://my.scu.edu.cn/",
    "Upgrade-Insecure-Requests": "1"
}
sdk = muggle_ocr.SDK(model_type=muggle_ocr.ModelType.Captcha)
with open("config.txt", "r", encoding='utf-8') as f:
    info = f.readlines()
j_username = info[0].strip('\n')
j_password = info[1].strip('\n')
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



# 这个函数用来获取所有的已选课程的信息
def getAlreadyCourseInfo(session):
    already_select_course_info_list = []
    try:
        response = session.get(url=already_select_course_url, headers=header).text
    except Exception as error:
        print(error)




def main(session):
    # ------------login-------------
    while True:
        # 登录
        # loginResponse = login2(session)
        loginResponse = login1(session)
        if loginResponse == "success":
            break
        else:
            print("登陆失败！")
            time.sleep(2)

    """# ----------login_end------------

    # -----------------------已选课程-----------------------------------
    print("\n=====================已选课程如下=====================\n")
    for each_course_info in getAlreadyCourseInfo(session):
        print("课程名:" + each_course_info[0] + " 任课教师:" + each_course_info[1] +
              " 课程号_课序号:" + each_course_info[2] + "_" + each_course_info[3])
    print("\n=====================已选课程如上=====================\n")"""
    content = session.get(url=already_select_course_url, headers=header).text
    my_course = json.loads(content)
    

if __name__ == "__main__":
    session = requests.session()
    main(session)
