from django.db import models


# Create your models here.
class MyCourse(models.Model):  # 继承了django的基类Model

    course_id = models.CharField(max_length=255)
    kch = models.CharField(max_length=255)
    kxh = models.CharField(max_length=255)
    kcm = models.CharField(max_length=255)
    zxjxjhh = models.CharField(max_length=255)
    skjs = models.CharField(max_length=255)
    kkxy = models.CharField(max_length=255)
    classWeek = models.CharField(max_length=255)
    classDay = models.IntegerField()
    classSessions = models.IntegerField()
    continuingSession = models.IntegerField()

    def __str__(self):
        return self.kcm + " --- " + self.skjs


class AllCourse(models.Model):  # 继承了django的基类Model

    course_id = models.CharField(max_length=255)
    kch = models.CharField(max_length=255)
    kxh = models.CharField(max_length=255)
    kcm = models.CharField(max_length=255)
    zxjxjhh = models.CharField(max_length=255)
    skjs = models.CharField(max_length=255)
    kkxy = models.CharField(max_length=255)
    classWeek = models.CharField(max_length=255)
    classDay = models.IntegerField()
    classSessions = models.IntegerField()
    continuingSession = models.IntegerField()

    def __str__(self):
        return self.kcm + " --- " + self.skjs
