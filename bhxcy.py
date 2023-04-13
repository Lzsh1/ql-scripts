import requests
from urllib.parse import urlencode
import json
url = 'https://gms.ihaoqu.com/gmswx/app.php?rid=28&ogid=10&noauth=1&r=api2&apiAction=SignIn'
headers = {'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}
data = {
    "uid": "",
    "token": "",
    "signure": ""
}
#使用的是 'application/x-www-form-urlencoded' 格式传递数据，那么需要将请求数据构造为 key=value 的形式，并使用 urlencode() 方法对其进行编码
encoded_data = urlencode(data)
#post上面的url并带上参数
response = requests.post(url=url, headers=headers, data=encoded_data)
#先对response.content以 UTF-8 的编码方式进行解码再使用json.loads()方法将解码后的字符串转化成一个 JSON 对象
result = json.loads(response.content.decode('utf-8'))
#打印result中的msg
print(result['msg'])
