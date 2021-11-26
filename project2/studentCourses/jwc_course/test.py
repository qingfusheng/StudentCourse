import base64

import requests
import json

import requests.exceptions

"""
GET https://rt3.map.gtimg.com/tile?styleid=0&tiles=12_3230_2415,12_3231_2415,12_3230_2414,12_3231_2414&version=919&style=100&compress=1&mapType=hybrid HTTP/1.1
Host: rt3.map.gtimg.com
Connection: keep-alive
Accept: application/json
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Accept-Language: en-us,en


"""
url = "https://rt3.map.gtimg.com/tile?styleid=0&tiles=12_3230_2415,12_3231_2415,12_3230_2414,12_3231_2414&version=919&style=100&compress=1&mapType=hybrid"
header={
    "Host": "rt3.map.gtimg.com",
    "Connection": "keep-alive",
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-us,en"
}
res = requests.get(url, headers=header)
content = json.loads(res.text)["datas"][0]["data"].encode()
decode_dict = base64.decodebytes(content)
print(decode_dict.decode("gbk", "ignore"))