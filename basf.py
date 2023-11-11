##巴斯夫最强安全大脑校园版
##欢迎大家加入“巴斯夫一体化基地(广东)有限公司”
##本脚本可完成巴斯夫最强安全大脑校园版的每日答题每天十分，但还是希望大家认真学习安全知识，认真贯彻巴斯夫理念
##抓包获取gc-eassistance.basf.com下的cookie与ua即可

import json
import requests
import time
import os

cookies = os.getenv('basf')


class InvalidURLException(Exception):
    pass


class BASF:
    def __init__(self, cookie1):
        self.question_answers = []
        self.headers = {
            "Host": "gc-eassistance.basf.com",
            "X-CSRF-TOKEN": "OXlO-Mp2yPom5ONAA-1atWVVKA1a_VpjnA6DRIZSF6w",
            "Accept-Language": "zh-CN,zh-Hans;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Cookie": cookie1.split("#")[0],
            "Connection": "keep-alive",
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.34(0x18002231) NetType/WIFI Language/zh_CN",
            "Referer": "https://gc-eassistance.basf.com/h5/headline/",
            "X-USER-ID": "",
            "X-Requested-With": "XMLHttpRequest"
        }
        self.exam_questions_url = "https://gc-eassistance.basf.com/api/gear-campus-quiz/daily-exam/start"
        self.answer_url = "https://gc-eassistance.basf.com/api/gear-campus-quiz/learning/answer"
        self.submit_url = "https://gc-eassistance.basf.com/api/gear-campus-quiz/daily-exam/complete"

    def answer(self, questions=None):
        self.question_answers = []
        response = requests.post(self.exam_questions_url, headers=self.headers)
        if response.status_code == 200:
            data = json.loads(response.text)
            try:
                questions = data['data']['questions']
                self.examId = data['data']['examId']

                # 遍历每个问题，发送 POST 请求提交问题答案，并将问题 ID 和正确答案保存到 question_answers 数组中，以备后续使用
                for question in questions:
                    question_id = question['id']
                    payload = {
                        "id": question_id,
                        "userAnswer": [1]
                    }
                    response = requests.post(self.answer_url, headers=self.headers, json=payload)
                    if response.status_code == 200:
                        answer_data = json.loads(response.text)
                        if 'data' in answer_data and 'answer' in answer_data.get('data', {}):
                            user_answer = answer_data['data']['answer']
                            self.question_answers.append({
                                "id": question_id,
                                "userAnswer": user_answer
                            })
                        else:
                            print("Error: JSON 字段错误")
                    else:
                        print("Error: ", response.status_code)
            except KeyError:
                print("今日答题已完成")


    def submit(self):
        questions = []
        print("question_answers:", self.question_answers)
        payload = {
            "userAnswers": [
                {
                    "id": self.question_answers[0]['id'],
                    "userAnswer": self.question_answers[0]['userAnswer']
                },
                {
                    "id": self.question_answers[1]['id'],
                    "userAnswer": self.question_answers[1]['userAnswer']
                },
                {
                    "id": self.question_answers[2]['id'],
                    "userAnswer": self.question_answers[2]['userAnswer']
                },
                {
                    "id": self.question_answers[3]['id'],
                    "userAnswer": self.question_answers[3]['userAnswer']
                },
                {
                    "id": self.question_answers[4]['id'],
                    "userAnswer": self.question_answers[4]['userAnswer']
                },
                {
                    "id": self.question_answers[5]['id'],
                    "userAnswer": self.question_answers[5]['userAnswer']
                },
                {
                    "id": self.question_answers[6]['id'],
                    "userAnswer": self.question_answers[6]['userAnswer']
                },
                {
                    "id": self.question_answers[7]['id'],
                    "userAnswer": self.question_answers[7]['userAnswer']
                },
                {
                    "id": self.question_answers[8]['id'],
                    "userAnswer": self.question_answers[8]['userAnswer']
                },
                {
                    "id": self.question_answers[9]['id'],
                    "userAnswer": self.question_answers[9]['userAnswer']
                }
            ],
            "examId": self.examId
        }

        # 发送 POST 请求提交考试答案
        response = requests.post(self.submit_url, headers=self.headers, json=payload)
        if response.status_code == 200:
            print(response.text)
            print(f'账号{index}每日答题提交成功')
        else:
            print("每日考试提交失败。")

    def run(self):
        self.answer()
        if self.question_answers is not None:
            self.submit()


if __name__ == "__main__":
    user_cookie = cookies.split('@')
    print(f"巴斯夫答题共获取到{len(user_cookie)}个账号")
    try:
        for index, cookie in enumerate(user_cookie, start=1):
            print(f"=========开始第{index}个账号=========")
            BASF(cookie).run()
            time.sleep(1)
    except InvalidURLException as e:
        print(str(e))
