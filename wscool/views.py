from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

# 1.定义视图函数
def index(request):
    return HttpResponse('老铁')
