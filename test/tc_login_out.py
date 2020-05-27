from pprint import pprint
import json

import requests

#  测试登陆
# payload = {
#     'username': 'wscool',
#     'password': 'dell@2018'
# }
#
# response = requests.post('http://127.0.0.1:8000/api/mgr/signin', data=payload)
# pprint(response.json())

#########################################################

# 测试logout
# response = requests.get('http://127.0.0.1:8000/api/mgr/signout')
# pprint(response.json())


#########################################################

# 测试显示用户列表
# listcustomer = {
#     'action': 'list_customer'
# }
# requestsession = requests.session()
# response = requestsession.get('http://127.0.0.1:8000/api/mgr/customers', params=listcustomer)
# pprint(response.json())

##########################################################
# 测试添加客户
#
# payload = {
#     'action': 'add_customer',
#     'data': {
#         'name': 'wilson, liu',
#         'phonenumber': '0592-8185662',
#         'address': '厦门市湖里区金尚路2388号'
#     }
# }
#
# j = json.dumps(payload)
# headers = {'Content-Type': 'application/json'}
# requestsession = requests.session()
# response = requestsession.post('http://127.0.0.1:8000/api/mgr/customers', headers=headers, data=j)
# pprint(response.json())

##########################################################
# 测试删除客户

# payload = {
#     'action': 'del_customer',
#     'id': 1
# }
#
# j = json.dumps(payload)
# headers = {'Content-Type': 'application/json'}
#
# response = requests.post('http://127.0.0.1:8000/api/mgr/customers', headers = headers, data=j)
# pprint(response.json())


##########################################################
# 测试修改客户

payload = {
    'action': 'modify_customer',
    'id': 3,
    'newdata': {
        'name': 'tracy_zhou'
    }
}

j = json.dumps(payload)
headers = {'Content-Type': 'application/json'}

response = requests.post('http://127.0.0.1:8000/api/mgr/customers', headers=headers, data=j)
pprint(response.json())
