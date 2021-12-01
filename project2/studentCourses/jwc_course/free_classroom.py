import requests


def find_free_classroom(jxl="yjA"):
    url = " https://cypcc.cn/pennisetum/classroom/jxldata?jxlname=" + jxl
    res = requests.get(url)
    room_info = res.json()
    return room_info

