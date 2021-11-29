import requests
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
url = "http://127.0.0.1:8000/get/"
header = {
        "Origin":"localhost",
        "Content-Type": "application/json"
}
res = requests.post(url, data=data, headers=header)
print(res.text)
