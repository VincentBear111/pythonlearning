age = input("请输入你的年龄：")

if int(age) > 18:
    print(f"我已经{age}岁了，马上步入大学生活了。")
else:
    print(f"我才{age}岁，还得{18-int(age)}年才能去上大学。")

print("希望时间过得慢些吧！")


"""
案例：
1. 通过input语句，获取键盘输入，为age变量赋值。
2. 通过if判断是否是成年人，满足条件则输出提示信息
"""

print("欢迎来到黑马儿童游乐场，儿童免费，成人收费。")
age = input("请输入你的年龄：")

if (int(age) > 18):
    print(f"您现在{int(age)}岁了，已经成年，需要补票10元。")
else:
    print(f"您现在{int(age)}岁了，还未成年，可以免费游玩。")

print("祝您玩的愉快！")