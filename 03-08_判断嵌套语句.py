print("欢迎来到黑马动物园游玩。")

if int(input("请输入你的身高（cm）：")) > 120:
    print("不好意思，你的身高超标了，不可以免费。")
    print("不过如果你的vip等级大于3也还是可以免费游玩的。")

    if int(input("请输入你的vip等级(1~5)：")) > 3:
        print("恭喜您，您可以免费游玩。")
    else:
        print("不好意思，你的条件都不满足，不能免费游玩。")

        name = input("请问您是否愿意继续游玩？")
        if name == '是':
            print("祝您玩的愉快")
        else:
            print("很遗憾，这次不能免费游玩，欢迎您下次来玩。")
    
else:
    print("祝您玩的愉快")