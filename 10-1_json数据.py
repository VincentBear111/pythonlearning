"""
json数据与python数据相互转换
"""
import json

data = [{"name":"张大山", "age":18}, {"name":"王大锤", "age":17}, {"name":"赵小虎", "age":12}]

# 将python数据(字符串)转换为json数据, 使用 json.dumps()方法
json_str = json.dumps(data, ensure_ascii=False)     # ensure_ascii 参数可以正常显示中文
print(type(json_str))
print(json_str)

# 将json数据转换为python数据(字符串), 使用json.loads()方法
s = '[{"name":"张大山", "age":18}, {"name":"王大锤", "age":17}, {"name":"赵小虎", "age":12}]'
l = json.loads(s)
print(type(l))
print(l)