import os
import requests
import json

def sign_in():
    account = os.environ.get('BHXCY')
    uid, token, signure = account.split(':')

    url = 'https://gms.ihaoqu.com/gmswx/app.php?rid=28&ogid=10&noauth=1&r=api2&apiAction=SignIn'
    headers = {'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}
    data = {
        "uid": uid,
        "token": token,
        "signure": signure
    }
    encoded_data = urlencode(data)
    response = requests.post(url=url, headers=headers, data=encoded_data)
    result = json.loads(response.content.decode('utf-8'))
    print(result['msg'])

if __name__ == '__main__':
    sign_in()
    

