from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):  # 继承了django的基类Model
    # "用户学习的主题"
    text = models.CharField(max_length=200)
    date_added = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        # "返回模型的字符串表示"
        return self.text


class Entry(models.Model):
    # "学到某个主题的具体知识"
    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING)  # 外键是一个数据库术语，它引用了数据库中的另一条记录
    text = models.TextField()
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "entries"
        """我们在Entry类中嵌套了Meta类。Meta存储用于管理模型的额外信息，在这python manage.py makemigrations app_name里，它让
我们能够设置一个特殊属性，让Django在需要时使用Entries来表示多个条目。如果没有这个类，
Django将使用Entrys来表示多个条目"""
    def __str__(self):
        if len(self.text)>50:
            return self.text[:50] + "..."
        else:
            return self.text
