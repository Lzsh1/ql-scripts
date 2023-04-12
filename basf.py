import requests

url = "https://gc-eassistance.basf.com/api/gear-campus-quiz/daily-exam/start"
headers = {
    "Cookie": "",
    "User-Agent": "",
}

response = requests.get(url, headers=headers)
question_ids = [item["id"] for item in response.json()["data"]["questions"]]

answers = {}  # 存储答案

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
