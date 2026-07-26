from curl_cffi import requests
import json

res_sum = 0

session = requests.Session()

cookies = {
    'Hm_lvt_f80b2b389f44bbfb3bfe1704817d44e0': '1784967969,1785030148',
     'HMACCOUNT': 'BD910D236505039B',
    'sessionid': 'z3rt2u2qt1fzr84o9v3r23p1ggostpzs',
     'Hm_lpvt_f80b2b389f44bbfb3bfe1704817d44e0': '1785035781'
}

# 先访问主页，使用登录Cookie
main_page = "https://match.yuanrenxue.cn/match/19"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36 Edg/150.0.0.0',
}

# 设置cookies到session
for key, value in cookies.items():
    session.cookies.set(key, value)

main_resp = session.get(main_page, headers=headers, impersonate="chrome110")
# print(f"Main page status: {main_resp.status_code}")

all_numbers = []

for i in range(1, 6):
    url = "https://match.yuanrenxue.cn/api/question/19?page={}&pageSize=10&kw=".format(i)

    # 第5页用特殊UA
    if i == 5 :
        ua = 'yuanrenxue'
    else:
        ua='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36 Edg/150.0.0.0'

    headers = {
        'User-Agent': ua,
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'https://match.yuanrenxue.cn/match/19',
        'sec-ch-ua': '"Not;A=Brand";v="8", "Chromium";v="150", "Microsoft Edge";v="150"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    try:
        resp = session.get(url, headers=headers, impersonate="chrome110")
        print(f"\nPage {i}: Status {resp.status_code}")
        print(f"Response: {resp.text}")

        if resp.status_code == 200:
            data = resp.json()
            # 只取数字
            numbers = []  # 创建一个空列表，用于存储提取的数字

            # 遍历 data['data'] 中的每一个元素
            for x in data['data']:
                # 检查当前元素 x 是否是整数(int)或浮点数(float)类型
                if isinstance(x, (int, float)):
                    # 如果是数字类型，就添加到 numbers 列表中
                    numbers.append(x)
                # 如果不是数字类型（比如字符串、布尔值等），就跳过，不处理
            page_sum = sum(numbers)
            res_sum += page_sum
            all_numbers.extend(numbers)
            print(f"Numbers: {numbers}")
            print(f"Page sum: {page_sum}")

    except Exception as e:
        print(f"Error on page {i}: {e}")

#打印结果
print(f"All numbers: {all_numbers}")
print(f"Total sum: {res_sum}")


