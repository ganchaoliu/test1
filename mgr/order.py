import json

from django.db import transaction
from django.db.models import F
from django.http import JsonResponse, HttpRequest

from common.models import Order, OrderMedicine


# 返回信息格式
# {
#     "ret": 0,
#     "retlist": [
#         {
#             "id": 1,
#             "name": "华山医院订单001",
#             "create_date": "2018-12-26T14:10:15.419Z",
#             "customer_name": "华山医院",
#             "medicinelist": [
#                 {"id":16,"amount":5,"name":"环丙沙星"},
#                 {"id":15,"amount":5,"name":"克林霉素"}
#             ]
#         },
#         {
#             "id": 2,
#             "name": "华山医院订单002",
#             "create_date": "2018-12-27T14:10:37.208Z",
#             "customer_name": "华山医院",
#             "medicinelist": [
#                 {"id":11,"amount":3,"name":"青霉素"},
#                 {"id":15,"amount":5,"name":"克林霉素"}
#             ]
#         }
#     ] ,
#     'total': 2
# # }

def listorder(request):
    qs = Order.objects \
        .annotate(
        customer_name=F('custom__name'),
        medicines_name=F('medicines__name'),
        amount=F('ordermedicine__amount')) \
        .values('id', 'name', 'create_date', 'medicines__id', 'medicines_name', 'amount')
    retList = list(qs)

    # newList=[]
    # medicinelist = {}
    # for order in retList:
    #     order

    newlist = []
    id2order = {}
    for one in retList:
        orderid = one['id']
        if orderid not in id2order:
            id2order[id] = orderid
            medicine = dict()
            medicine['id'] = one[id]
            medicine['name'] = one['medicines_name']
            medicine['amount'] = one['amount']
            one['medicinelist'].append(medicine)
            newlist.append(one)
        else:
            medicine = dict()
            medicine['id'] = one[id]
            medicine['name'] = one['medicines_name']
            medicine['amount'] = one['amount']
            one['medicinelist'].append(medicine)

    print(retList)
    return JsonResponse({'ret': 0, 'retlist': retList})

    # 前端传进来的数据格式为：
    # {
    #     'action':'add_order',
    #     'data':{
    #         'name':'wscool的订单',
    #         'customer_id' : 3,
    #         'medicines' : [
    #             {
    #             'medicine_id':1,
    #             'amount': 5
    #             },
    #             {
    #                 'medicine_id': 2,
    #                 'amount': 5
    #             }
    #         ]
    #     }
    # }


def addorder(request):
    print("下单############################################################")
    info = request.params['data']
    name = info['name']
    customer_id = info['customerid']
    medicines = info['medicinelist']

    with transaction.atomic():
        neworder = Order.objects.create(name=name, custom_id=customer_id)
        bactch = list()
        for medicine in medicines:
            om = OrderMedicine(order_id=neworder.id, medicine_id=medicine['id'], amount=1)
            bactch.append(om)
        OrderMedicine.objects.bulk_create(bactch)

    return JsonResponse({'ret': 0, 'id': neworder.id, 'msg': '下单成功'})


def modifyorder(request):
    info = request.params['newdata']
    id = request.params['id']
    try:
        order = Order.objects.get(id=id)
    except Order.DoesNotExist:
        return {
            'ret': 1,
            'msg': f'id为‘{id}’的订单不存在'
        }
    if 'name' in info:
        order.name = info['name']
    if 'sn' in info:
        order.sn = info['sn']
    if 'description' in info:
        order.description = info['description']
    order.save()
    return JsonResponse({'ret': 0, 'msg': "订单已更新"})


def del_order(request):
    print('###############################################')
    orderid = request.params['id']
    try:
        order = Order.objects.get(id=orderid)
    except Order.DoesNotExist:
        return JsonResponse({
            'ret': 1,
            'msg': f'id为‘{orderid}’的订单不存在'
        })
    order.delete()
    return JsonResponse({'ret': 0})


def dispatcher(request):
    if 'usertype' not in request.session:
        return JsonResponse({'ret': 302,
                             'msg': '未登陆',
                             'redirect': 'mgr/sign.html'},
                            status=302)
    if request.session['usertype'] != 'mgr':
        return JsonResponse({'ret': 302,
                             'msg': '用户非mgr类型',
                             'redirect': 'mgr/sign.html'},
                            status=302)

    if request.method == 'GET':
        request.params = request.GET
    elif request.method in ['POST', 'PUT', 'DELETE']:
        request.params = json.loads(request.body)

    action = request.params['action']
    if action == 'list_order':
        return listorder(request)
    elif action == 'add_order':
        return addorder(request)
    elif action == 'modify_order':
        return modifyorder(request)
    elif action == 'del_order':
        return del_order(request)
    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型请求'})
