# 测试显示用户列表
import json
from pprint import pprint

import requests

# 测试显示药品列表
# listmedicine= {
#     'action': 'list_medicine'
# }
# requestsession = requests.session()
# response = requestsession.get('http://127.0.0.1:8000/api/mgr/medicines', params=listmedicine)
# pprint(response.json())

# 添加药品
# data = {
#     'action': 'add_medicine',
#     'data': {
#         'name': '感冒灵冲剂',
#         'sn': '00352655478',
#         'description': 'OTC药品'
#     }
# }
#
# senddata = json.dumps(data)
#
# headers = {'Content-Type': 'application/json'}
# requestsession = requests.session()
# response = requestsession.post('http://127.0.0.1:8000/api/mgr/medicines', headers=headers, data=senddata)
# pprint(response.json())


# 测试删除药品

# payload = {
#     'action': 'del_medicine',
#     'id': 4
# }
#
# j = json.dumps(payload)
# headers = {'Content-Type': 'application/json'}
#
# response = requests.post('http://127.0.0.1:8000/api/mgr/medicines', headers = headers, data=j)
# pprint(response.json())

# 测试更新药品
# data = {
#     'action': 'modify_medicine',
#     'id': 1,
#     'newdata': {
#         'name': '感冒灵冲剂',
#         'description': 'OTC药品，可以在普通的药店买到'
#     }
# }
#
# senddata = json.dumps(data)
#
# headers = {'Content-Type': 'application/json'}
# requestsession = requests.session()
# response = requestsession.post('http://127.0.0.1:8000/api/mgr/medicines', headers=headers, data=senddata)
# pprint(response.json())



