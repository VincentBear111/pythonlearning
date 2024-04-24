"""
多个返回值：
按照返回值的顺序，写对应的多个变量接收即可
变量之间使用逗号（，）隔开
支持不同类型的return
"""
def test_return():
    return 1,2,3
x,y,z = test_return()
print(x)
print(y)
print(z)

"""
函数参数种类：
使用方式上不同，函数有4种常见参数使用方式：
1. 位置参数
2. 关键字参数
3. 缺省参数
4. 不定长参数
注意：函数调用时，如果有位置参数，位置参数必须在关键字参数的前面，但关键字参数之间不存在先后顺序
"""

# 不定长参数 - 位置不定长   " * "号
# 不定长定义的形式参数会作为元组存在，接收不定长数量的参数传入
def user_info(*args):
    print(f"args参数的类型是：{type(args)}, 内容是：{args}")

user_info("小明", 20, "男")

# 不定长 -- 关键字不定长， " ** "号
def user_info(**kwargs):
    print(f"kwargs参数的类型是：{type(kwargs)}, 内容是：{kwargs}")

user_info(name='bear', age=30, gender='男', address='南京')


"""
匿名函数：将函数自身作为参数传入另一个函数内
将函数传入的作用在于：传入计算逻辑，而非传入数据
"""
print("===============[匿名函数]===============")
def test_func(compute):
    res = compute(1,2)
    print(res)

def compute(x, y):
    return x + y

test_func(compute)