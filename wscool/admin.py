from django.contrib import admin

# Register your models here.
from wscool.models import pic_info, group, wadmin


# 自定义模型管理类

class Pic_info_admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'file_type', 'create_date','owner_id']


admin.site.register(pic_info, Pic_info_admin)
admin.site.register(wadmin)
admin.site.register(group)