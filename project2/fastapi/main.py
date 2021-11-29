import uvicorn
import fastapi
from pydantic import BaseModel, validator, conint, constr

header = {
    "Host": "zhjwjs.scu.edu.cn",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "Accept-Language": "zh-CN,zh-Hans;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "http://zhjwjs.scu.edu.cn",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15",
    "Connection": "keep-alive",
}


class POST_INFO(BaseModel):
    zxjxjhh: str = ""
    kch: str = ""
    kcm: str = ""
    js: str = ""
    kkxs: str = ""
    skxq: str = ""
    skjc: str = ""
    xq: str = ""
    jxl: str = ""
    jas: str = ""
    pageNum: str = ""
    pageSize: str = ""
    kclb: str = ""


app = fastapi.FastAPI()  # 创建一个app实例


@app.get("/")  # 编写一个路径操作装饰器
async def root(href: str):  # 编写一个路径操作函数
    return {"你好！": "朋友。", "href": href}


@app.post("/")
async def root(href: str, request_data: POST_INFO):
    """print(POST_INFO)
    print(type(POST_INFO))"""
    return {"data":request_data.js}


if __name__ == '__main__':
    uvicorn.run(app='main:app', host="127.0.0.1", port=8080, reload=True, debug=True)
