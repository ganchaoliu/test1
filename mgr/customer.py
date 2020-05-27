import json

from django.http import JsonResponse, HttpRequest

from common.models import Customer


def listcustomer(request):
    qs = Customer.objects.values()
    retList = list(qs)
    return JsonResponse({'ret': 0, 'retlist': retList})


def addcustomer(request):
    info = request.params['data']
    record = Customer.objects.create(name=info['name'],
                                     phonenumber=info['phonenumber'],
                                     address=info['address'])
    return JsonResponse({'ret': 0, 'id': record.id})


def modifycustomer(request):
    info = request.params['newdata']
    id = request.params['id']
    try:
        customer = Customer.objects.get(id=id)
    except Customer.DoesNotExist:
        return {
            'ret': 1,
            'msg': f'id为‘{id}’的客户不存在'
        }
    if 'name' in info:
        customer.name = info['name']
    if 'phonenumber' in info:
        customer.phonenumber = info['phonenumber']
    if 'address' in info:
        customer.address = info['address']
    customer.save()
    return JsonResponse({'ret': 0, 'msg': "客户更新成功"})


def del_customer(request):
    customerid = request.params['id']
    try:
        customer = Customer.objects.get(id=customerid)
    except Customer.DoesNotExist:
        return JsonResponse({
            'ret': 1,
            'msg': f'id为‘{customerid}’的客户不存在'
        })
    customer.delete()
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
        a = request.params
        print('action = %s'%request.params['action'])


    action = request.params['action']
    if action == 'list_customer':
        return listcustomer(request)
    elif action == 'add_customer':
        return addcustomer(request)
    elif action == 'modify_customer':
        return modifycustomer(request)
    elif action == 'del_customer':
        return del_customer(request)
    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型请求'})
