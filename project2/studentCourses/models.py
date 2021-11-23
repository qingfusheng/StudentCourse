from django.db import models


# Create your models here.
class MyCourse(models.Model):  # 继承了django的基类Model

    course_id = models.CharField(max_length=255, null=True)
    kch = models.CharField(max_length=255, null=True)
    kxh = models.CharField(max_length=255, null=True)
    kcm = models.CharField(max_length=255, null=True)
    zxjxjhh = models.CharField(max_length=255, null=True)
    skjs = models.CharField(max_length=255, null=True)
    classWeek = models.CharField(max_length=255, null=True)
    classDay = models.IntegerField()
    classSessions = models.IntegerField()
    continuingSession = models.IntegerField()

    def __str__(self):
        return self.kcm + " --- " + self.skjs


class AllCourse(models.Model):  # 继承了django的基类Model

    course_id = models.CharField(max_length=255, null=True)
    kch = models.CharField(max_length=255, null=True)
    kxh = models.CharField(max_length=255, null=True)
    kcm = models.CharField(max_length=255, null=True)
    zxjxjhh = models.CharField(max_length=255, null=True)
    skjs = models.CharField(max_length=255, null=True)
    kkxy = models.CharField(max_length=255, null=True)
    classWeek = models.CharField(max_length=255, null=True)
    classDay = models.IntegerField()
    classSessions = models.IntegerField()
    continuingSession = models.IntegerField()

    def __str__(self):
        return self.kcm + " --- " + self.skjs
