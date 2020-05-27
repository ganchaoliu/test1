import datetime

from django.db import models


# 客户表
class Customer(models.Model):
    # 客户名称
    name = models.CharField(max_length=55)
    # 客户地址
    phonenumber = models.CharField(max_length=20)
    # 客户地址
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# 药品表
class Medicine(models.Model):
    name = models.CharField(max_length=55)

    sn = models.CharField(max_length=50)

    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# 订单表
class Order(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)

    # 外键关联Cusomer表的主键，如果删除外键对应的主键时
    # CASCADE 删除关联的所有数据
    # PROTECT 禁止删除，要求将订单中的记录删除了才可以删除主键
    # SET_NULL 将对应的外键设成为NULL，要求记录可以为NULL
    custom = models.ForeignKey(Customer, on_delete=models.PROTECT)
    create_date = models.DateTimeField(default=datetime.datetime.now)

    # 订单中多对多的关系，通过表'OrderMedicine'表关联，下面再定义这个表
    medicines = models.ManyToManyField(Medicine, through='OrderMedicine')

    def __str__(self):
        return self.name


class OrderMedicine(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    medicine = models.ForeignKey(Medicine, on_delete=models.PROTECT)
    # 订单中药品的数量
    amount = models.PositiveIntegerField()


class Country(models.Model):
    name = models.CharField(max_length=100)


class Student(models.Model):
    name = models.CharField(max_length=100)
    grade = models.PositiveSmallIntegerField()
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
