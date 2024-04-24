
if False:
    i = 0
    while i < 100:
        print("hello world")
        i += 1

"""

案例：求1-100的累加和
"""
if False:
    i = 0
    sum = 0
    while i <= 100:
        sum += i
        i += 1
    print(f"1-100的累加和为:{sum}")

"""
猜数字游戏：
设置一个1-100范围内的随机整数变量，通过while循环，配合input语句，判断输入的数字是否等于随机数
1. 无限次机会，直到猜中为止
2. 每一次猜不中，会提示大了或小了
3. 猜完数字后，提示猜了多少次
"""
if False:
    import random

    num = random.randint(1, 100)

    count = 0
    while True:
        guess_num = int(input("请输入您猜测的数字："))
        count += 1
        if guess_num == num:
            print(f"恭喜您，您猜中了！")
            break
        else:
            if guess_num > num:
                print(f"您当前猜测的数字是{guess_num}，大了")
            else:
                print(f"您当前猜测的数字是{guess_num}，小了")

    print(f"恭喜您，猜中了，当前数字为{num}， 您一共猜了{count}次。")

"""
while循环嵌套案例：
打印九九乘法表
"""

i = 1
while i < 10:

    j = 1
    while j <= i:
        # 通过制表符 \t 对齐； 参数 end='' : 可以让字符串不换行
        print(f"{j} * {i} = {i*j}\t", end='')
        j += 1

    i += 1
    print("\n")

print("Finshed!")