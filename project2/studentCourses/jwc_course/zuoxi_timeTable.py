import requests
from bs4 import BeautifulSoup

def get_zuoxi_time_table():
    url = "https://jwc.scu.edu.cn/info/1001/7048.htm"
    res = requests.get(url, verify=False)
    text = res.content.decode("utf-8-sig").encode("utf-8").decode("utf-8")
    with open("1.html", "w", encoding="utf-8") as f:
        f.write(text)
    soup = BeautifulSoup(text, features="lxml")
    elems = soup.find_all("div", attrs={"class": "v_news_content"})
    content = str(elems[0])
    return content

