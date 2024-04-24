"""
input语句（函数）
前面学习过的print语句，可以完成将内容（字面量、变量等）输出到屏幕上
在python中，与之对应的还有一个input语句，用来获取键盘输入。
数据输出：print
数据输入：input
使用上也非常简单：
* 使用input()语句可以从键盘获取输入
* 使用一个变量接收（存储）input语句获取的键盘输入数据即可
"""

print("请告诉我你是谁？")
name = input()
print(f"我知道了，你是{name}.")

# 输入数字类型
num = input("请输入您的银行卡密码：")
print(f"你的银行密码是{num}，此处的数据类型为{type(name)}.")
num = int(num)
print(f"当前数据类型为{type(num)}")