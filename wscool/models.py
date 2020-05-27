from django.db import models


# Create your models here.
# 图片类


class wadmin(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    # 管理员名字
    def __str__(self):
        return self.name


class pic_info(models.Model):
    '''图片模型类'''
    name = models.CharField(max_length=30)
    file_type = models.CharField(max_length=10)
    create_date = models.DateField()
    owner = models.ForeignKey("wadmin", on_delete=models.DO_NOTHING)

    # 返回文件名
    def __str__(self):
        return self.name


class group(models.Model):
    name = models.CharField(max_length=30)
    comments = models.CharField(max_length=255)

    # 返回组名
    def __str__(self):
        return self.name
