import requests
import json

exam_questions_url = "https://gc-eassistance.basf.com/api/gear-campus-quiz/daily-exam/start"
answer_url = "https://gc-eassistance.basf.com/api/gear-campus-quiz/daily-exam/answer"
submit_url = "https://gc-eassistance.basf.com/api/gear-campus-quiz/daily-exam/complete"
headers = {
    "Cookie": "",
    "User-Agent": "",
}

# 获取每日考试的问题ID和对应答案
response = requests.get(exam_questions_url, headers=headers)

if response.status_code == 200:
    data = json.loads(response.text)
    questions = data['data']['questions']

    # 用于存储问题ID和答案
    question_answers = []
    for question in questions:
        question_id = question['id']
        payload = {
            "id": question_id,
            "userAnswer": [1]
        }
        response = requests.post(answer_url, headers=headers, json=payload)
        if response.status_code == 200:
            answer_data = json.loads(response.text)
            answer = answer_data['data']['correct']
            question_answers.append({
                "id": question_id,
                "userAnswer": [answer]
            })
        else:
            print("Error: ", response.status_code)
else:
    print("Error: ", response.status_code)

# 构建新的请求主体
payload = {
    "userAnswers": [
        {
            "id": question_answers[0]['id'],
            "userAnswer": [data1]
        },
        {
            "id": question_answers[1]['id'],
            "userAnswer": [data2]
        },
        {
            "id": question_answers[2]['id'],
            "userAnswer": [data3]
        },
        {
            "id": question_answers[3]['id'],
            "userAnswer": [data4]
        },
        {
            "id": question_answers[4]['id'],
            "userAnswer": [data5]
        },
        {
            "id": question_answers[5]['id'],
            "userAnswer": [data6]
        },
        {
            "id": question_answers[6]['id'],
            "userAnswer": [data7]
        },
        {
            "id": question_answers[7]['id'],
            "userAnswer": [data8]
        },
        {
            "id": question_answers[8]['id'],
            "userAnswer": [data9]
        },
        {
            "id": question_answers[9]['id'],
            "userAnswer": [data10]
        }
    ],
    "examId": 42763
}

# 提交每日考试
response = requests.post(submit_url, headers=headers, json=payload)

if response.status_code == 200:
    print("每日考试提交成功！")
else:
    print("每日考试提交失败。")
