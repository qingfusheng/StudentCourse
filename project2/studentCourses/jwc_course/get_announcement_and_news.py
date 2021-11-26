from bs4 import BeautifulSoup
import requests


def get_tonggao():
    url = "https://jwc.scu.edu.cn/"
    res = requests.get(url, verify=False)
    text = res.content.decode("utf-8-sig").encode("utf-8").decode("utf-8")
    soup = BeautifulSoup(text, features="lxml")
    tonggao = soup.find("ul", attrs={"class": "list-llb-s"}).find_all("li", attrs={"class": "list-llb-list"})
    tonggao_list = []
    for each in tonggao:
        href = each.find("a").get("href")
        if "https://www.scu.edu.cn/" in href:
            href=href
        else:
            href="https://www.scu.edu.cn/"+href
        title = each.find("a").get("title")
        content = each.find("span").string.replace("\n", "").replace("\r", "").replace(" ", "")
        time = each.find("em", attrs={"class": "fr list-date-a"}).string
        tonggao_list.append((href, title, content, time))
    return tonggao_list


def get_news_report():
    url = "https://jwc.scu.edu.cn/"
    res = requests.get(url, verify=False)
    text = res.content.decode("utf-8-sig").encode("utf-8").decode("utf-8")
    soup = BeautifulSoup(text, features="lxml")
    news_report = soup.find("ul", attrs={"class":"list-llc-two"}).find_all("li")
    news_list = []
    for each in news_report:
        href = each.find("a").get("href")
        if "https://www.scu.edu.cn/" in href:
            href=href
        else:
            href="https://www.scu.edu.cn/"+href
        title = each.find("a").get("title")
        content = each.find("a").text.replace("\n", "").replace("\r", "").replace(" ", "")
        news_list.append((href, title, content))
        print(href, title, content)
    return news_list

def get_yiqing_zhuanlan():
    url = "https://jwc.scu.edu.cn/"
    res = requests.get(url, verify=False)
    text = res.content.decode("utf-8-sig").encode("utf-8").decode("utf-8")
    soup = BeautifulSoup(text, features="lxml")
    yiqing = soup.find("ul", attrs={"class": "list-llc-one"}).find_all("li")
    yiqing_list = []
    for each in yiqing:
        href = each.find("a").get("href")
        if "https://www.scu.edu.cn/" in href:
            href = href
        else:
            href = "https://www.scu.edu.cn/" + href
        title = each.find("a").get("title")
        content = each.find("a").text.replace("\n", "").replace("\r", "").replace(" ", "")
        yiqing_list.append((href, title, content))
        print(href, title, content)
    return yiqing_list

