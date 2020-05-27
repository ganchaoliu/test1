import json

from django.db.models import F
from django.http import JsonResponse, HttpRequest

from common.models import Medicine


def listmedicine(request):
    qs = Medicine.objects.annotate(desc=F('description')).values('id', 'name', 'desc', 'sn')
    retList = list(qs)
    print(retList)
    return JsonResponse({'ret': 0, 'retlist': retList})


def addmedicine(request):
    info = request.params['data']
    if info['name'] == "":
        return JsonResponse({'ret': 1, 'msg': '名字不为空'})

    record = Medicine.objects.create(name=info['name'],
                                     sn=info['sn'],
                                     description=info['desc'])
    return JsonResponse({'ret': 0, 'id': record.id})


def modifymedicine(request):
    info = request.params['newdata']
    id = request.params['id']
    try:
        medicine = Medicine.objects.get(id=id)
    except Medicine.DoesNotExist:
        return {
            'ret': 1,
            'msg': f'id为‘{id}’的药品不存在'
        }
    if 'name' in info:
        medicine.name = info['name']
    if 'sn' in info:
        medicine.sn = info['sn']
    if 'desc' in info:
        medicine.description = info['desc']
    medicine.save()
    return JsonResponse({'ret': 0, 'msg': "药品已更新"})


def del_medicine(request):
    medicineid = request.params['id']
    try:
        medicine = Medicine.objects.get(id=medicineid)
    except Medicine.DoesNotExist:
        return JsonResponse({
            'ret': 1,
            'msg': f'id为‘{medicineid}’的药品不存在'
        })
    medicine.delete()
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
    if action == 'list_medicine':
        return listmedicine(request)
    elif action == 'add_medicine':
        return addmedicine(request)
    elif action == 'modify_medicine':
        return modifymedicine(request)
    elif action == 'del_medicine':
        return del_medicine(request)
    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型请求'})
