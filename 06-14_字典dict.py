"""
字典的定义：
同样使用{}，不过存储的元素是一个个的：键值对，语法如下：
{key:value, key:value, ... , key:value}
字典中的key值不允许重复

字典不支持下标索引
支持for循环，不支持while循环
"""


# 定义空的字典
my_dict = {}
my_dict = dict()

# 定义嵌套字典
"""
姓名        语文    数学    英语
王力宏      77      66      33
周杰伦      88      86      55
林俊杰      99      96      66
"""
stu_score_dict = {
    "王力宏":{"语文":77, "数学":66, "英语":33},
    "周杰伦":{"语文":88, "数学":86, "英语":55},
    "林俊杰":{"语文":99, "数学":96, "英语":66}
}

# 获取嵌套字典数据
score = stu_score_dict["周杰伦"]["语文"]
print(score)

# 字典的常用操作
my_dict = {"周杰伦":99, "林俊杰":88, "张学友":77}
print(f"原始字典{my_dict}")

# 新增元素
my_dict["张信哲"] = 66
print(f"新增元素后的字典{my_dict}")

# 更新元素
my_dict["周杰伦"] = 37
print(f"新增元素后的字典{my_dict}")

# 删除元素      .pop(元素)
score = my_dict.pop("周杰伦")
print(f"删除元素后的字典{my_dict}，\n周杰伦的分数为{score}")

# 清空元素      .clear()

# 获取字典中全部的key     字典.keys()
keys = my_dict.keys()
print(keys)

# 字典的遍历
# 方式1：通过获取到全部的key来完成遍历
for key in keys:
    print(f"字典的key是{key}")
    print(f"字典的value是{my_dict[key]}")

# 方式2：直接对字典进行for循环
for key in my_dict:
    print(f"2字典的key是{key}")
    print(f"2字典的value是{my_dict[key]}")


# 统计字典的元素数量    len()函数 
    
# sorted()函数排序，排序结果会变为列表，将元素存在列表容器里