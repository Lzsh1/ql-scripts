##巴斯夫最强安全大脑
##本脚本仅供参考学习，如被开除请自行承担后果
##抓包获取gc-eassistance.basf.com下的cookie填写在第15行
##多账号版本暂时删除
import requests
import json
exam_questions_url = "https://gc-eassistance.basf.com/api/quiz/daily-exam/start"
answer_url = "https://gc-eassistance.basf.com/api/quiz/learning/answer"
submit_url = "https://gc-eassistance.basf.com/api/quiz/daily-exam/complete"
headers = {
    "Host": "gc-eassistance.basf.com",
    "X-CSRF-TOKEN": "OXlO-Mp2yPom5ONAA-1atWVVKA1a_VpjnA6DRIZSF6w",
    "Accept-Language": "zh-CN,zh-Hans;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Cookie": "",
    "Connection": "keep-alive",
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.34(0x18002231) NetType/WIFI Language/zh_CN",
    "Referer": "https://gc-eassistance.basf.com/h5/headline/",
    "X-USER-ID": "",
    "X-Requested-With": "XMLHttpRequest"
}

question_answers = []
# 发送 GET 请求获取每日考试的问题和答案
response = requests.post(exam_questions_url, headers=headers)

if response.status_code == 200:
    data = json.loads(response.text)
    questions = data['data']['questions']
    examId = data['data']['examId']

    # 遍历每个问题，发送 POST 请求提交问题答案，并将问题 ID 和正确答案保存到 question_answers 数组中，以备后续使用
    for question in questions:
        question_id = question['id']
        payload = {
            "id": question_id,
            "userAnswer": [1]
        }
        response = requests.post(answer_url, headers=headers, json=payload)
        if response.status_code == 200:
            answer_data = json.loads(response.text)
            if 'data' in answer_data and 'answer' in answer_data.get('data', {}):
                user_answer = answer_data['data']['answer']
                question_answers.append({
                    "id": question_id,
                    "userAnswer": user_answer
                })
            else:
                print("Error: JSON 字段错误")
        else:
            print("Error: ", response.status_code)
else:
    print("Error: ", response.status_code)

# 打印 question_answers 列表
print(question_answers)

if len(questions) != len(question_answers):
    print("Error: 问题数和答案数不匹配。")
    exit()

# 构建新的请求主体，包含用户回答的所有问题和对应的答案
if len(question_answers) == len(questions):
    payload = {
        "userAnswers": [
            {
                "id": question_answers[0]['id'],
                "userAnswer": question_answers[0]['userAnswer']
            },
            {
                "id": question_answers[1]['id'],
                "userAnswer": question_answers[1]['userAnswer']
            },
            {
                "id": question_answers[2]['id'],
                "userAnswer": question_answers[2]['userAnswer']
            },
            {
                "id": question_answers[3]['id'],
                "userAnswer": question_answers[3]['userAnswer']
            },
            {
                "id": question_answers[4]['id'],
                "userAnswer": question_answers[4]['userAnswer']
            },
            {
                "id": question_answers[5]['id'],
                "userAnswer": question_answers[5]['userAnswer']
            },
            {
                "id": question_answers[6]['id'],
                "userAnswer": question_answers[6]['userAnswer']
            },
            {
                "id": question_answers[7]['id'],
                "userAnswer": question_answers[7]['userAnswer']
            },
            {
                "id": question_answers[8]['id'],
                "userAnswer": question_answers[8]['userAnswer']
            },
            {
                "id": question_answers[9]['id'],
                "userAnswer": question_answers[9]['userAnswer']
            }
        ],
        "examId": examId
    }

    # 发送 POST 请求提交考试答案
    response = requests.post(submit_url, headers=headers, json=payload)
    if response.status_code == 200:
        print(response.text)
        print("每日考试提交成功！")
    else:
        print("每日考试提交失败。")
else:
    print("无法构建提交请求：问题答案数与问题数不匹配。")


