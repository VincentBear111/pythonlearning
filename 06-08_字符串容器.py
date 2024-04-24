"""
字符串的下标（索引）：
和其他容器如：列表、元组一样，字符串也可以通过下标进行访问
1. 从前向后，下标从0开始；
2. 从后向前，下标从-1开始；

*** 同元组一样，字符串也是一个**无法修改**的数据容器

所以，以下操作均是不允许的：
1. 修改指定下标的字符
2. 移除特定下标的字符
3. 追加字符等
"""

my_str = 'itheima and itcast'
# 通过下标索引取值
value = my_str[2]
value2 = my_str[-16]
print(f"value:{value}\nvalue2:{value2}")

# index方法
print("----------index方法----------------")
idx = my_str.index('and')
print(idx)


"""
字符串的替换
语法：字符串replace（字符串1，字符串2）
功能：将字符串内的全部：字符串1， 替换为字符串2
注意：不是修改字符串本身，而是得到了一个新的字符串。
"""

my_str = 'bear'
new_str = my_str.replace('be', "bear")
print(new_str)

"""
字符串的分割：
语法：字符串.split（分隔符字符串）
功能：按照指定的分隔符字符串，将字符串划分为多个字符串，并存入列表对象中
注意：字符串本身不变，而是得到了一个列表对象
"""
my_str = 'hello python itheima itcast'
print(my_str)
str_list = my_str.split(' ')
print(str_list)

"""
字符串的规整操作（去除前后空格）
语法：字符串.strip()
字符串的规整操作（去除前后指定字符串）
语法：字符串.strip(字符串)
"""
my_str = '   12itheima12   '
print(my_str)
new_str = my_str.strip()
print(new_str)

new_str = new_str.strip('12')
print(new_str)

count = new_str.count('it')
print(count)
