from django.db import models


# Create your models here.

# 创建用户表


class User(models.Model):
    user = models.CharField('用户名', max_length=50, null=False)
    password = models.CharField('密码', max_length=100, null=False)
    email = models.CharField('邮箱', max_length=50, null=True)
    time = models.DateTimeField('注册时间', auto_now=True)

    def __str__(self):
        return self.user
