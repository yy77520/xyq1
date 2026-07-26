import requests
import csv

url = 'https://www.questnutrition.com/collections/protein-bars-all/products.json'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    'cookie': 'cart_currency=USD; _shopify_y=9a297566-5b89-46ac-bc50-37065bc6e604; _shopify_s=ea4ac5c3-4bfc-4ca2-ad38-1e751737cacf; _shopify_essential=:AZ-XOi1EAAEAiw4Oswt6ngeSJjt6vIckvm3WhMxQ6O-MS3TEe1omwiCNXy7NRJjT8s9iARLXl9jzMc9ebZE3K1q9-p8kjH_iMDInsUEKBCR8cgFh8mASORW36CYgoCxutsQ3RvPSquXfXTApwOKwPEAujMnyWQiCzlBY9gQSpvgilHzTnKGWPOFoDrZ2RywsD4ENp-jygMtmVkZMbKIxzW13LsONFzRLsYcuewWjdJ8-vhFZUd9OxkS7XipS_byr3MD1QFPjB76C1r29AjLqv5GB8cigVZuUKlhQlkzu9rEHkzY5Nfpg69DIGCq2fmyh5osrWEi9UU5_FXw:; _shopify_analytics=:AZ-XOi21AAEAsNERzVeaHxOoaxywEOHTrOTERoAHe4cTHKfLtwyC3fIVCZXL29i_2hWodbTQ1jBq3KmxW-9oJ319:; _shopify_marketing=:AZ-XOi22AAEA9n0uz9zHpJRggv_2pBCTeoVCvLcoWq3bKZ70adho0Uqk74w7sxpB4nqCt4SJoM60AvFvj9g5yJur:'
}

# 发送请求
res = requests.get(url, headers=headers)
response = res.json()['products']

# 创建一个列表来存储要写入CSV的数据
list = []

# 循环遍历所有产品
for product in response:
    handle = product['handle']
    title = product['title']

    # 收集所有变体ID
    list_ids = []
    variants = product['variants']
    for variant in variants:
        list_ids.append(str(variant['id']))
    print(list_ids)

    # 用逗号连接所有ID
    ids_str = ','.join(list_ids)
    # print(ids_str)
    # 添加到数据列表
    list.append([handle, title, ids_str])

    #查看打印结果
    # print(handle,title,ids_str)

# 保存到CSV文件
# with open('products.csv', 'w', newline='', encoding='utf-8-sig') as f:
#     writer = csv.writer(f)
#     # 写入表头
#     writer.writerow(['handle', 'title', 'id'])
#     # 写入数据
#     writer.writerows(list)



