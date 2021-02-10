import json


data = {'host': 'smtp.qq.com',
        'user': '',
        'password': '',
        'sender': '',
        'receivers': ['']}
with open('config.json', 'w') as f:
    data = json.dump(data,f)