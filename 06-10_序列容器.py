"""
序列
序列是指：内容连续、有序，可使用下标索引的一类数据容器
例如：列表、元组、字符串，均可以视为序列
语法：序列[起始位置:结束位置:步长]
"""
# 序列的切片操作

# 1. 对list进行切片，从1开始，4结束，步长为1
my_list = [0,1,2,3,4,5,6]
res1 = my_list[1:4]         # 步长默认是1，可以省略不写
print(f"结果1：{res1}")

# 2. 对tuple进行切片，从头开始，到最后结束，步长1
my_tuple = (0,1,2,3,4,5,6)
res2 = my_tuple[:]
print(f"结果2：{res2}")

# 3. 对str进行切片，从头开始，到最后结束，步长2
my_str = 'itheima and itcast'
res3 = my_str[::2]
print(f"结果3：{res3}")

# 4. 对str进行切片，从头开始，到最后结束，步长-1
res4 = my_str[::-1]     # 功能：反转字符串
print(f"结果4：{res4}")

# 5. 对列表进行切片，从3开始，到1结束，步长-1
res5 = my_list[3:1:-1]
print(f"结果5：{res5}")

# 6. 对元组进行切片，从头开始，到尾结束，步长-2
res6 = my_tuple[::-2]
print(f"结果6：{res6}")

new_str = '学python，来黑马程序员，月薪过万'
res = new_str[::-1]     # 功能：反转字符串
print(f"res:{res}")
new_res = res[9:4:-1]
print(f"new_res:{new_res}")