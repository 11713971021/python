from django.db import models
from userinfo.models import User

# Create your models here.


class Blogs(models.Model):
    title = models.CharField('标题', max_length=200, null=False)
    times = models.CharField('时间', max_length=30, null=False)
    body = models.TextField('正文', max_length=1000, null=False)
    # 第二个参数是，当USER　表中删除一条数据对应，ＢＬＯＧＳ数据也被删除
    bu = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
