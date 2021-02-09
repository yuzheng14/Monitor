import json


data = {'host': 'smtp.qq.com',
        'user': '',
        'password': '',
        'sender': '',
        'receivers': ['']}
with open('email.json', 'w') as f:
    data = json.dump(data,f)