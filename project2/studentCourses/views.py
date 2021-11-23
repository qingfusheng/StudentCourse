from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'studentCourses/index.html')

def mycourse(request):
    return render(request, 'studentCourses/mycourse.html')

def allcourse(request):
    return render(request, 'studentCourses/allcourse.html')

def helloParams(request):
    p1 = request.GET.get('p1')
    p2 = request.GET.get('p2')
    if not p1 or not p2:
        return HttpResponse("错误的参数请求")
    return HttpResponse("p1 = " + p1 + "; p2 = " + p2)