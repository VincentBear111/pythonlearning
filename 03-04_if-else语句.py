print("欢迎来到黑马儿童游乐场，儿童免费，成人收费。")
age = input("请输入你的年龄：")

if (int(age) > 18):
    print(f"您现在{int(age)}岁了，已经成年，需要补票10元。")
else:
    print(f"您现在{int(age)}岁了，还未成年，可以免费游玩。")

print("祝您玩的愉快！")


print("------------------------------------------------------")
print("欢迎来到黑马动物园")
height = input("请输入你的身高(cm)：")
vip_level = input("请输入您的vip等级（1~5）：")

if float(height) < 120:
    print("您的身高不够120cm，可以免费游玩。")
elif int(vip_level) > 3:
    print("您的vip级别大于3，可以免费游玩。")
else:  
    print("不好意思，您不够免费游玩的条件，需要话费10元购票游玩。")

print("祝您玩得愉快！")

if float(height) < 120 or int(vip_level) > 3:
    print("可以免费游玩。")
else:
    print("不可以免费游玩")