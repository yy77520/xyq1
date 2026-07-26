lst = [3, 1, 2, 3, 4, 1, 2]
#方法一 利用集合的去重性 然后结合列表 完成操作
data_set= set()
result = []
for item in lst:
    # print(item)
    if item not in data_set:
        data_set.add(item)
        result.append(item)
print(result)

#方法二 先利用fromkeys方法准换为字典，且利用了字典特性去重
dict=dict.fromkeys(lst)
# print(dict)
result1=list(dict.keys())
print(result1)


#方法三 利用枚举法根据数字和下标的位置来去重
result2=[]
for i ,items in enumerate(lst):
    if lst.index(items)==i:
        result2.append(items)
print(result2)