"""
数据容器分类：
列表（list）、元组（tuple）、字符串（str）、集合（set）、字典（dict）
"""

name_list = []
name_list = list()
name_list = ['itheima', 'itcast', 'python']
print(name_list)
print(type(name_list))
print(name_list[0])
print(name_list[1])
print(name_list[2])

# 注意：列表可以一次存储多个数据，而且可以是不同的数据类型，支持嵌套
my_list = ['hello', 666, 1.12, True]
print(my_list)
print(type(my_list))

print(len(my_list))
# for i in my_list:
#     print(i)

print(my_list[-1])

# 列表的常用操作
"""
列表的常用功能：
1. 插入元素
2. 删除元素
3. 清空列表
4. 修改元素
5. 统计元素个数
"""

print(my_list)
# 查询功能
print("列表中的查询功能：")
idx = my_list.index(666)
print(idx)

print("----修改列表元素-----")
my_list[1] = 555
print(my_list)

print("-----插入元素------")
# 列表.insert(下标，元素)，在指定下标位置，插入指定的元素
my_list.insert(4, "world")
print(my_list)

print("---------追加元素----------")
my_list.append(666)
print(my_list)

print("----------追加元素方式2-----------")
# 语法：列表.extend(其它数据容器)，将其他数据容器内容取出，依次追加到列表尾部
my_list.append([5,6,7])
my_list.extend([5,6,7])
print(my_list)

my_list = ['hello', 666, 1.12, True]
print(my_list)
print("-----元素的删除------")
del my_list[2]
print(my_list)
element = my_list.pop(1)
print(my_list)
print(element)

print("---------删除列表指定元素--------")
# remove方法：列表.remove(元素)
my_list = ['hello', 666, 1.12, True]
my_list.remove(1.12)
print(my_list)

print("------清空列表--------------")
my_list.clear()
print(my_list)

print("-------统计某一个元素在列表内的数量--------")
# count方法：列表.count(元素)
my_list = ['hello', 666, 1.12, True, 666]
count = my_list.count(666)
print(count)