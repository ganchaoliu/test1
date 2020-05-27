import json
from pprint import pprint

import requests

# data = {
#     'action': 'add_order',
#     'data': {
#         'name': 'wscool的订单',
#         'customer_id': 3,
#         'medicines': [
#             {
#                 'medicine_id': 1,
#                 'amount': 5
#             },
#             {
#                 'medicine_id': 2,
#                 'amount': 5
#             }
#         ]
#     }
# }
#
# j = json.dumps(data)
#
# headers = {'Content-Type': 'application/json'}
# requestsession = requests.session()
# response = requestsession.post('http://127.0.0.1:8000/api/mgr/orders', headers=headers, data=j)
# pprint(response.json())

data = {
    'action': 'list_order',
    'id': 3
}

j = json.dumps(data)

headers = {'Content-Type': 'application/json'}
requestsession = requests.session()
response = requestsession.post('http://127.0.0.1:8000/api/mgr/orders', headers=headers, data=j)
pprint(response.json())
