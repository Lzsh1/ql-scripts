# -*- coding: utf-8 -*-
'''
cron: 1 6,22 * * *
@Lzsh1
new Env('微信阅读');

微信打开 https://wi53988.jinzivps.top:10251/yunonline/v1/auth/372ebf1f87d26b5af3162691ad1793fd?codeurl=wi53988.jinzivps.top:10251&codeuserid=2&time=1692179287
抓取 http://1692180512.yykd202312.cloud任意链接下cookie的参数，只要ysm_uid=后面的参数
变量名为 read 多账号使用@隔开
export read=""
'''
import requests
import logging
import time
import os, re
from notify import send
from urllib.parse import parse_qs, urlparse
# 创建日志记录器
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

cookies = []
try:
    if "read" in os.environ:
        cookies = os.environ["read"].split("@")
        if len(cookies) > 0:
            logger.info(f"共找到{len(cookies)}个账号 已获取并使用Env环境Cookie")
            logger.info("声明：此脚本为python学习，请勿用于非法用途")
    else:
        logger.info("ck好像不对")
        exit(3)
except Exception as e:
    logger.error(f"发生错误：{e}")
    exit(3)


# -------------------------分割线------------------------
class miniso:
    @staticmethod
    def setHeaders(i):
        unionid = cookies[i]
        return unionid

    @staticmethod
    def gainuk(unionid):
        try:
            url = f'http://1692180512.yykd202312.cloud/yunonline/v1/wtmpdomain'
            payload = {
                "unionid": unionid,
            }
            r = requests.post(url, data=payload)
            response_json = r.json()
            url_query_string = response_json['data']['domain']
            params = parse_qs(urlparse(url_query_string).query)
            uk = params.get('uk', [''])[0]
            if uk:
                miniso.geturl(uk)
            else:
                print('ck填写错误')
        except Exception as e:
            print(e)

    @staticmethod
    def geturl(uk):
        try:
            url = f'https://nsr.zsf2023e458.cloud/yunonline/v1/do_read?uk=' + uk
            response = requests.get(url=url)
            result = response.json()
            if result['errcode'] == 0:
                link = result['data']['link']
                headers = {
                    "Host": "1691500721.yykd202312.cloud",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                    "Upgrade-Insecure-Requests": "1",
                    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.40(0x1800282a) NetType/WIFI Language/zh_CN",
                    "Accept-Language": "zh-CN,zh-Hans;q=0.9",
                    "Accept-Encoding": "gzip, deflate",
                    "Connection": "keep-alive"
                }
                requests.get(url=link, headers=headers)
                res = f"获取到阅读文章，正在阅读请稍后......"
                logger.info(res)
                time.sleep(8)  # 休眠3秒
                miniso.Read(uk)
            else:
                res = f"阅读: {result['msg']}"
                logger.info(res)
                log_list.append(res)
        except Exception as e:
            print(e)

    @staticmethod
    def Read(uk):
        try:
            url = f'https://nsr.zsf2023e458.cloud/yunonline/v1/get_read_gold'
            params = {
                'uk': uk,
                'time': '7',
                'timestamp': int(time.time() * 1000)
            }
            response = requests.get(url, params=params)
            result = response.json()
            if result['errcode'] == 0:
                res = f"获得{result['data']['gold']}金币，当前金币{result['data']['last_gold']}"
                logger.info(res)
                time.sleep(6)  # 休眠20秒
                miniso.geturl(uk)
            else:
                res = f"阅读: {result['msg']}"
                logger.info(res)
                log_list.append(res)
        except Exception as e:
            print(e)

    @staticmethod
    def tx(unionid):
        url = 'http://1692180032.yykd202312.cloud/yunonline/v1/gold'
        params = {
            'unionid': unionid,
            'timestamp': int(time.time() * 1000)
        }
        r = requests.get(url, params=params)
        res = f"当前共{r.json()['data']['last_gold']}金币\n今日共获得{r.json()['data']['day_gold']}金币"
        logger.info(res)
        log_list.append(res)
        if int(r.json()['data']['last_gold']) > 3000:
            url = 'http://1692180272.yykd202312.cloud/yunonline/v1/user_gold'
            params = {
                "unionid": unionid,
                "request_id": "73efdd34f13d6d3fa05de5fd3d5081d8",
                "gold": "3000"
            }
            r = requests.post(url, params=params)
            res = f"提现成功0.3成功"
            logger.info(res)
            log_list.append(res)
        else:
            print('金额不足提现')



if __name__ == '__main__':
    log_list = []  # 存储日志信息的全局变量
    for i in range(len(cookies)):
        logger.info(f"\n开始第{i + 1}个账号")

        logger.info("--------------快鸭阅读任务开始--------------")
        unionid = miniso.setHeaders(i)
        miniso.gainuk(unionid)
        miniso.tx(unionid)

    logger.info("\n============== 推送 ==============")
    send("快鸭阅读", '\n'.join(log_list))