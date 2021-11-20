from django.contrib import admin
from studentCourses.models import MyCourse, AllCourse
# Register your models here.
admin.site.register(MyCourse)
admin.site.register(AllCourse)