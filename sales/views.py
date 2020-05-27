from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from common.models import Customer


def listorders(request):
    return HttpResponse("下面是系统中所有的订单信息00")


def listcustomers(request):
    qs = Customer.objects.values()

    # request.GET是一个字典

    ph = request.GET.get('qq', None)
    if ph and ph!= "":
        qs = qs.filter(qq=ph)
    else:
        return HttpResponse("参数错误")

    retStr = ''
    for customer in qs:
        for name, value in customer.items():
            retStr += f'{name}:{value}|'
            retStr += '<br />'

        retStr += "<h5>××××××××××××华丽的分割线××××××××××××××</h5>"
    return HttpResponse(retStr)
