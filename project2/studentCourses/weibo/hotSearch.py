import json
import random
import re
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr
import requests


def Login_and_Get_HotSearch():
    genvisitor_url = "https://passport.weibo.com/visitor/genvisitor"
    header = {
        "Host": "passport.weibo.com",
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "sec-ch-ua": "\"Google Chrome\";v=\"95\", \"Chromium\";v=\"95\", \";Not A Brand\";v=\"99\"",
        "Content-Type": "application/x-www-form-urlencoded",
        "If-Modified-Since": "0",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
        "sec-ch-ua-platform": "\"Windows\"",
        "Accept": "*/*",
        "Origin": "https://passport.weibo.com",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://passport.weibo.com/visitor/visitor?entry=miniblog&a=enter&url=https%3A%2F%2Fs.weibo.com%2Ftop%2Fsummary&domain=.weibo.com&sudaref=&ua=php-sso_sdk_client-0.6.29&_rand=1636545384.2475",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }
    _data = {"cb": "gen_callback",
             "fp": {"os": "1",
                    "browser": "Chrome95,0,4638,69",
                    "fonts": "undefined", "screenInfo": "1920*1080*24",
                    "plugins": "Portable Document Format::internal-pdf-viewer::PDF Viewer|Portable Document Format::internal-pdf-viewer::Chrome PDF Viewer|Portable Document Format::internal-pdf-viewer::Chromium PDF Viewer|Portable Document Format::internal-pdf-viewer::Microsoft Edge PDF Viewer|Portable Document Format::internal-pdf-viewer::WebKit built-in PDF"
                    }
             }
    res = requests.post(genvisitor_url, headers=header, data=_data)
    # print(res.status_code)
    # print(res.text)
    reg = re.compile(r'window.gen_callback && gen_callback\((.*)\)')
    temp = json.loads(reg.findall(res.text)[0])["data"]
    confidence = ""
    tid = temp["tid"]
    if temp["new_tid"] is False:
        w = '2'
        confidence = str(temp["confidence"])
    else:
        w = '3'
    visit_url = "https://passport.weibo.com/visitor/visitor?a=incarnate&t=" + tid + "&w=" + w + "&c=" + confidence + "&gc=&cb=cross_domain&from=weibo&_rand=" + str(
        random.random())
    header2 = {
        "Host": "passport.weibo.com",
        "Connection": "keep-alive",
        "sec-ch-ua": "\"Google Chrome\";v=\"95\", \"Chromium\";v=\"95\", \";Not A Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
        "sec-ch-ua-platform": "\"Windows\"",
        "Accept": "*/*",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Dest": "script",
        "Referer": "https://passport.weibo.com/visitor/visitor?entry=miniblog&a=enter&url=https%3A%2F%2Fs.weibo.com%2Ftop%2Fsummary&domain=.weibo.com&sudaref=&ua=php-sso_sdk_client-0.6.29&_rand=1636545384.2475",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": "tid=" + tid + "__" + confidence
    }
    res = requests.get(visit_url, headers=header2)
    reg = re.compile(r'window.cross_domain && cross_domain\((.*)\)')
    sub = json.loads(reg.findall(res.text)[0])["data"]["sub"]
    subp = json.loads(reg.findall(res.text)[0])["data"]["subp"]
    header_summary = {
        "Host": "s.weibo.com",
        "Connection": "keep-alive",
        "sec-ch-ua": "\"Google Chrome\";v=\"95\", \"Chromium\";v=\"95\", \";Not A Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://passport.weibo.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": "SUB=" + sub + "; SUBP=" + subp
    }
    summary_url = "https://s.weibo.com/top/summary"
    res = requests.get(summary_url, headers=header_summary)
    html = res.text
    return html


def requests_news():
    while True:
        try:
            html = Login_and_Get_HotSearch()
            break
        except Exception as error:
            continue
    reg = re.compile(
        r'<td class="td-01.*?">(.*)?</td>[\s]+<td class="td-02">[\s]+<a href(_to)?=\"(.*)?\" [h|t].*>(.*)</a>(.*)[\s]+<span>(.*)</span>[\s]+.*[\s]+</td>[\s]+<td class="td-03">(<i.*>(.*)</i>)?</td>')
    elems = reg.findall(html)

    hot_search = list()
    for elem in elems:
        order = elem[0]
        if len(elem[0]) == 1:
            order = '0'+order
        temp = (order, "https://s.weibo.com/" + elem[2], elem[3], elem[5], elem[7])
        if temp[3] == " ":
            continue
        hot_search.append(temp)
    return hot_search


def get_html():
    hot_search = requests_news()
    html_up = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>微博热搜推送</title></head><body><div style="font-size: larger;"><table summary="热搜"><caption style="font-family: 楷体;font-size: xx-large;">微博热搜</caption><tr><th>序号</th><th>热搜内容</th><th>热度</th><th>附加</th></tr>'
    html_down = '</table></div></body></html>'
    html_center = ""
    for i in hot_search:
        html_center = html_center + '<tr><td style="text-align: center;">' + i[
            0] + '</td><td style="text-align: center;"><a href="' + i[1] + '"/>' + i[
                          2] + '</td><td style="text-align: center;">' + i[
                          3] + '</td><td style="text-align: center;">' + i[4] + '</td></tr>'
    html = html_up + html_center + html_down
    return html
