#悦动群AppStore下载抓ydq.yichengwangluo.net下的Authorization参数
#推荐单号单ip
import requests
import time
import os

cookies = os.getenv('ydq_ck')


class InvalidURLException(Exception):
    pass


class User:

    def __init__(self, cookie1):
        self.header = {
            "Host": "ydq.yichengwangluo.net",
            "Authorization": cookie1.split("#")[0],
        }
        ##气泡红包90分钟一秒10次上限好像
    def qphb(self):
        r = requests.post('https://ydq.yichengwangluo.net/api/v2/reward/bubble?', headers=self.header)
        if r.json().get('code') == 0:
            reward = r.json().get('result').get('coin')
            coupon = r.json().get('result').get('coupon')
            print(f'获得{reward}金币/获得{coupon}提现券')
        elif r.json().get('code') == 40302:
            print('气泡红包时间未到')
        elif r.json().get('code') == 40301:
            print('气泡红包已达上限')
        else:
            print(r.text)
    def hby(self):
        r = requests.post("https://ydq.yichengwangluo.net/api/v2/reward/rain?", headers=self.header)
        if r.json().get('code') == 0:
            reward = r.json().get('result').get('coin')
            coupon = r.json().get('result').get('coupon')
            print(f'获得{reward}金币/获得{coupon}提现券')
        elif r.json().get('code') == 40302:
            print('红包雨时间未到')
        elif r.json().get('code') == 40301:
            print('红包雨已达上限')
        else:
            print(r.text)

    def cg(self):
        for i in range(7):
            payload = {
                "no": str(i + 1),
            }
            r = requests.post('https://ydq.yichengwangluo.net/api/v2/reward/barrier/index?', headers=self.header,data=payload)
            if r.json().get('code') == 0:
                reward = r.json().get('result').get('coin')
                coupon = r.json().get('result').get('coupon')
                fragment = r.json().get('result').get('fragment')
                print(f'第{i+1}次闯关获得{reward}金币/获得{coupon}提现券/获得{fragment}iPhone14碎片')
            elif r.json().get('code') == 40301:
                print('今日闯关已达上限')
                break
            else:
                print(f'闯关出错{r.text}')
                break

    def kgg(self):
        for i in range(10):
            r = requests.post("https://ydq.yichengwangluo.net/api/v2/zhuan/video?", headers=self.header)
            if r.json().get('result').get('ticket') is not None:
                ticket = r.json().get('result').get('ticket')
                url = 'https://ydq.yichengwangluo.net/api/v2/ads/action/completed?ticket=' + ticket + '&channel=2&transid=54716D7B-3805-46DF-93DC-483330DE19A8&platformname=pangle&class=10000&type=9&tid=354377514388316160&ecpm=32704.1&'
                res = requests.get(url, headers=self.header)
                if res.json().get('code') == 0:
                    reward = res.json().get('result').get('reward')
                    coupon = res.json().get('result').get('coupon')
                    print(f'第{i+1}次看广告获得{reward}金币/获得{coupon}提现券')
                    print('等待35秒')
                    time.sleep(35)
                else:
                    print(res.text)
                    break
            else:
                print(r.text)
                break

    def ksp(self):
        for i in range(10):
            r = requests.get("https://ydq.yichengwangluo.net/api/v2/video/coin?short=1&", headers=self.header)
            if r.json().get('result').get('ticket') is not None:
                ticket = r.json().get('result').get('ticket')
                url = " https://ydq.yichengwangluo.net/api/v2/video/coin?ticket=" + ticket + "&short=1&"
                res = requests.get(url, headers=self.header)
                if res.json().get('code') == 0:
                    reward = res.json().get('result').get('reward')
                    print(f'第{i+1}次刷视频获得{reward}金币')
                    print('等待30秒')
                    time.sleep(30)
                else:
                    print(res.text)
                    break
            else:
                print(r.text)
                break
    def receive(self):
        payload = {
            "id": '7',
        }
        r = requests.post('https://ydq.yichengwangluo.net/api/v2/zhuan/done?', headers=self.header, data=payload)
        if r.json().get('result').get('message') == '领取成功':

            print('刷视频奖励领取成功')

    def info(self):
        r = requests.get('https://ydq.yichengwangluo.net/api/v2/member/profile?debug=0&', headers=self.header)
        if r.json().get('code') == 0:
            uuid = r.json().get('result').get('uuid')
            name = r.json().get('result').get('nickname')
            balance = r.json().get('result').get('balance')
            coupon = r.json().get('result').get('ticket')
            today_point = r.json().get('result').get('today_point')
            fragment = r.json().get('result').get('fragment')
            print(f'uuid{uuid}账号{name}-当前余额{balance}元-提现券{coupon}张\n今日已赚{today_point}金币-再凑{200-fragment}碎片召唤iPhone14')
        else:
            print(r.text)

    def signin(self):
        r = requests.post('https://ydq.yichengwangluo.net/api/v2/reward/sign?', headers=self.header)
        if r.json().get('code') == 0:
            reward = r.json().get('result').get('coin')
            coupon = r.json().get('result').get('coupon')
            print(f'获得{reward}金币/获得{coupon}提现券')
        else:
            print(r.text)

    def run(self):
        self.info()
        time.sleep(2)
        r = requests.post("https://ydq.yichengwangluo.net/api/v2/zhuan/index?", headers=self.header)
        task_list = r.json().get('result').get('items')
        for item in task_list:
            if item["id"] == 9 and item["st"] == 0:
                self.kgg()
            if item["id"] == 7 and item["st"] == 0:
                self.ksp()
            if item["id"] == 7 and item["st"] == 1:
                self.receive()
            if item["id"] == 10 and item["st"] == 0:
                self.signin()
        self.cg()
        self.hby()
        self.qphb()

if __name__ == "__main__":
    user_cookie = cookies.split('\n')
    print(f"悦动群获取到{len(user_cookie)}个账号")
    try:
        for index, cookie in enumerate(user_cookie, start=1):
            print(f"=========开始第{index}个账号=========")
            User(cookie).run()
    except InvalidURLException as e:
        print(str(e))

