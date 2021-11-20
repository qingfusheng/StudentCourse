from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'studentCourses/index.html')

def mycourse(request):
    return render(request, 'studentCourses/mycourse.html')

def allcourse(request):
    return render(request, 'studentCourses/allcourse.html')