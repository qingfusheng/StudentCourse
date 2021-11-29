from django.core.checks import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_protect
"""
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
"""

def getContent(request):
    if request.method == "POST" and request.POST:
        post_content = {}
        zxjxjhh = request.POST.get("zxjxjhh")
        kch = request.POST.get("kch")
        kcm = request.POST.get("kcm")
        js = request.POST.get("js")
        kkxs = request.POST.get("kkxs")
        skxq = request.POST.get("skxq")
        skjc = request.POST.get("skjc")
        xq = request.POST.get("xq")
        jxl = request.POST.get("jxl")
        jas = request.POST.get("jas")
        pageNum = request.POST.get("pageNum")
        pageSize = request.POST.get("pageSize")
        kclb = request.POST.get("kclb")
        post_content = {"zxjxjhh":zxjxjhh,
                       "kch": kch,
                       "kcm":kcm,
                       "js":js,
                       "kkxs":kkxs,
                       "skxq":skxq,
                       "skjc":skjc,
                       "xq":xq,
                       "jxl":jxl,
                       "jas":jas,
                       "pageNum":pageNum,
                       "pageSize":pageSize,
                       "kclb":kclb,
                       }
        print(post_content)
        ret = 1
        if ret == 1:
            response = HttpResponseRedirect('/')

        elif ret == 0:
            messages.error(request, "用户或密码不正确")
            return render(request, 'users/login.html')
        elif ret == -1:
            messages.error(request, "教务管理系统不可达,请稍后重试")
            return render(request, 'users/login.html')
    return HttpResponse({})
