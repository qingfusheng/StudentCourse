import requests
from bs4 import BeautifulSoup


def get_xiaoli():
    header = {
        "Host": "jwc.scu.edu.cn",
        "Connection": "keep-alive",
        "sec-ch-ua": "\"Google Chrome\";v=\"95\", \"Chromium\";v=\"95\", \";Not A Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Content-Type": "text/plain"
    }
    url = "https://jwc.scu.edu.cn/cdxl.htm"
    res = requests.get(url, headers=header, verify=False)
    html = res.text
    soup = BeautifulSoup(html, features='lxml')
    elems = soup.find_all("div", attrs={"class": "list-e-main"})
    url = "https://jwc.scu.edu.cn/" + elems[0].find("a").get("href")
    res = requests.get(url, headers=header, verify=False)
    soup = BeautifulSoup(res.text, features="lxml")
    elems = soup.find_all("div", attrs={"class": "v_news_content"})[0].find_all("p")
    imgs_urls = []
    for elem in elems:
        ret = elem.find("img")
        if ret:
            imgs_urls.append("https://jwc.scu.edu.cn" + ret.get("src"))
        else:
            continue
    return imgs_urls
