from django.contrib import admin

# Register your models here.
from common.models import *


# 自定义模型管理类

class Pic_info_admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phonenumber', 'address']


class Order_info_admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'create_date', 'custom_id']


class Medicine_info_admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'sn', 'description']


class OrderMedicine_info_admin(admin.ModelAdmin):
    list_display = ['id', 'order_id', 'medicine_id', 'amount']


admin.site.register(Customer, Pic_info_admin)
admin.site.register(Order, Order_info_admin)
admin.site.register(Medicine, Medicine_info_admin)
admin.site.register(OrderMedicine, OrderMedicine_info_admin)
