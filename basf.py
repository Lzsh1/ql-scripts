##巴斯夫最强安全大脑校园版
##已测试通过
##抓包获取gc-eassistance.basf.com下的cookie与ua即可
import requests
import json

exam_questions_url = "https://gc-eassistance.basf.com/api/gear-campus-quiz/daily-exam/start"
answer_url = "https://gc-eassistance.basf.com/api/gear-campus-quiz/learning/answer"
submit_url = "https://gc-eassistance.basf.com/api/gear-campus-quiz/daily-exam/complete"
headers = {
    "Cookie": "",
    "User-Agent": ""
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
print("question_answers:", question_answers)

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
