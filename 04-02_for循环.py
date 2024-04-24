"""
for循环：
除了while循环语句以外，python同样提供了for循环语句。
两者的功能基本差不多，但仍有一些区别：
1. while循环的循环条件是自定义的，自行控制循环条件；
2. for循环是一种“轮询”机制，是对一批内容的“逐个处理”
"""

name = "itheima"
for x in name:
    print(x)
print("finished.")

str_name = "itheima is a brand of itcast"
sum = 0
for x in str_name:
    if x == 'a':
        sum += 1
    else:
        continue
print(f"{str_name}字符串中共有{sum}个'a'")
print("finished!")


""""
for循环实现九九乘法表
"""
print("------for循环实现九九乘法表-----")
for i in range(1, 10, 1):
    for j in range(1, i+1, 1):
        print(f"{j} * {i} = {j*i}\t", end='')
    print()