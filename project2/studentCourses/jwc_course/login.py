import requests
from bs4 import BeautifulSoup
from users.storage.user_config import *


def check_valid(j_username, j_password):
    my_url = "http://my.scu.edu.cn/userPasswordValidate.portal"
    index_url = "http://zhjw.scu.edu.cn/index.jsp"
    login_url = "http://zhjw.scu.edu.cn/j_spring_security_check"
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
    session = requests.session()
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
        soup = BeautifulSoup(html, features="lxml")
        with open("1.html", "w", encoding="utf-8") as f:
            f.write(html)
        if "四川大学教务管理系统" in html:
            print("登陆成功")
            name = soup.find("span", attrs={"class": "user-info"}).text.replace("\n", "").replace("\r", "").replace(
                "\t", "").replace("欢迎您，", "")
            save_config(j_username, j_password, name)
            return 1
        else:
            print("密码错误")
            return 0
    except requests.exceptions or BaseException as error:
        print(error)
        return -1
