"""
集合：
集合不支持内部元素重复存在(自带去重功能)，并且内部元素是无序的
** 列表 []
** 元组 ()
** 字符串 ""
** 集合 {}
"""

my_set = {'itheima', 'itcast', '666','itheima', 'itcast', '666','itheima', 'itcast', '666'}
my_set_empty = set()
print(f"my_set的内容是{my_set}, 类型是{type(my_set)}.")
print(f"my_set_empty的内容是{my_set_empty}, 类型是{type(my_set_empty)}.")

"""
集合的常用操作--修改
首先，因为集合是无序的，所以集合不支持：下标索引访问
但是集合和列表一样，是允许修改的
"""
# 添加新元素    集合.add()方法
my_set.add('111')
print(f"my_set的add后内容是{my_set}, 类型是{type(my_set)}.")

# 移除元素  集合.remove(元素)方法
my_set.remove('111')
print(f"my_set的remove后内容是{my_set}, 类型是{type(my_set)}.")

# 从集合中随机取出元素      集合.pop()方法
ele = my_set.pop()
print(f"集合中随机取出的元素为：{ele}")
print(f"集合中随机取出的元素后的集合为：{my_set}")

# 清空集合      集合.clear()方法

# 计算两个集合的差集    集合1.difference(集合2)方法
# 功能：得到集合1中有而集合2中没有的元素
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.difference(set2)
print(f"差集为：{set3}")
print(f"集合1为：{set1}")
print(f"集合2为：{set2}")

# 消除两个集合的差集        集合1.difference_update(集合2)
# 功能：对比集合1和集合2，在集合1内，删除和集合2相同的元素
# 结果：集合1被修改，而集合2不变
set1.difference_update(set2)
print(f"集合1为：{set1}")
print(f"集合2为：{set2}")

# 集合合并      集合1.union(集合2)
# 功能：将集合1和集合2组合成新集合
# 结果：得到新集合，集合1和集合2不变
set1 = {1,2,3}
set2 = {1,5,6}
set4 = set1.union(set2)
print(f"并集为：{set4}")
print(f"集合1为：{set1}")
print(f"集合2为：{set2}")

# 统计集合的元素数量 len()

# 集合的遍历
# 集合不支持下标索引，不能使用while循环
# 但是可以使用for循环
set1 = {1,2,3}
for ele in set1:
    print(f"集合的元素有：{ele}")


"""
案例：
有如下列表对象：
my_list = ['黑马程序员', '传智播客', '黑马程序员'， '传智播客', 'itheima', 'itcast', 'itheima', 'itcast', 'best']
请：
1. 定义一个空集合
2. 通过for循环遍历列表
3. 在for循环中将列表的元素添加至集合
4. 最终得到元素去重后的集合对象，并打印输出
"""
print("===================================================")
my_list = ['黑马程序员', '传智播客', '黑马程序员', '传智播客', 'itheima', 'itcast', 'itheima', 'itcast', 'best']
my_set = set()
for ele in my_list:
    my_set.add(ele)

print(my_set)