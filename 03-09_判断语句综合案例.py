"""
案例要求：
1. 数字随机产生，1-10；
2. 有3次机会猜测数字，通过3层嵌套判断实现
3. 每次猜不中，会提示大了或小了
"""

import random

num = random.randint(1,10)
guess_num = int(input("请输入你猜测的数字："))

if guess_num == num:
    print("恭喜您，第一次就猜中了！")
else:
    if guess_num > num:
        print("您猜测的数字大了")
    else:
        print("您猜测的数字小了")

    guess_num = int(input("请再次输入你猜测的数字："))
    if guess_num == num:
        print("恭喜您，第二次就猜中了！")
    else:
        if guess_num > num:
            print("您猜测的数字大了")
        else:
            print("您猜测的数字小了")
        
        guess_num = int(input("请再次输入你猜测的数字："))
        if guess_num == num:
            print("恭喜您，第三次就猜中了！")
        else:
            print("不好意思，三次机会用完了，您都没猜中！")