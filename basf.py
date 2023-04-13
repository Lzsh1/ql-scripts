import requests

url = 'https://gc-eassistance.basf.com/api/gear-campus-quiz/daily-exam/start'
headers = {
    'User-Agent': '',
    'Cookie': ''
}

response = requests.post(url, headers=headers)##post考试的url
data = response.json()##将响应主体放到data

if "questions" not in data:##如果考试url中不存在questions则代表考试已完成，有则获取考试的问题id
    print("今日考试已完成")
else:
    id = data['questions']['id'][0]
    answers = {}
##将考试的问题id到每日学习的url进行查询答案，再输出答案
    for question_id in question_ids:
        data = {
            "id": str(question_id),
            "userAnswer": [1]
        }

        response = requests.post("https://gc-eassistance.basf.com/api/gear-campus-quiz/learning/answer", headers=headers, json=data)
        answer = response.json()["data"]["answer"][0]
        answers[str(question_id)] = answer

    print("问题的正确答案如下：")

    for question_id, answer in answers.items():
        print(f"问题 '{question_id}' 的正确答案是: {answer}")



