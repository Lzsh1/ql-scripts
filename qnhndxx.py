#应该全湖南的只要是青年湖南微信公众号都可用
#湖南石油化工职业技术学院湖南青年大学习可用
#填写11行的cookie和30行的ctoken
#ck一天有效别玩了！！！
import requests
import json

url = 'http://dxx.hngqt.org.cn/project/list'

# 这里填写请求头部信息
headers = {
    "Cookie": ""
}

# 发送 GET 请求，并获得响应数据
response = requests.post(url, headers=headers)
data = json.loads(response.text)

if response.status_code == 200:
    # 解析响应数据，获取最新的 5 个 project_id 值并替换掉 "http://dxx.hngqt.org.cn/study/studyAdd" 接口中的 projectId
    project_list = data['data']['list'][:5]
    latest_project_ids = [project['project_id'] for project in project_list]

    # 记录每个项目是否完成学习
    study_results = []

    # 发送 POST 请求到 "http://dxx.hngqt.org.cn/study/studyAdd" 接口，通过遍历 latest_project_ids 数组设置 data 中的 projectId
    for projectId in latest_project_ids:
        data = {
            'projectId': projectId,
            'ctoken': '',
            'captcha': ''
        }
        response = requests.post('http://dxx.hngqt.org.cn/study/studyAdd', data=data, headers=headers)
        if response.status_code == 200:
            result = json.loads(response.text)
            if result['code'] == 0 and result['success'] and not result['data']:
                study_results.append(True)  # 记录学习成功
            else:
                print(f"项目 ID 为 {projectId} 的学习未完成，返回结果为：{response.text}")
                study_results.append(False)  # 记录学习失败
        else:
            print(f"项目 ID 为 {projectId} 的学习请求失败，错误码为 {response.status_code}")
            study_results.append(False)  # 记录学习失败

    # 判断所有学习是否都完成
    if all(study_results):
        print("所有学习已完成")
    else:
        print("有学习未完成，请检查以上提示信息")
else:
    print("请求失败")
