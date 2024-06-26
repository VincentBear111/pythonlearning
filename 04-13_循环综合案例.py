"""
某公司，账户余额有1W元，给20名员工发工资。
1. 员工编号从1-20，从编号1开始，依次领取工资，每人可领取1000元
2. 领工资时，财务判断员工绩效分（1-10）（随机生成），如果低于5分，则不发工资，换下一位
3. 如果工资发完了，则结束发工资，等下个月
"""

# 账户余额
money = 10000
for i in range(1,21):
    import random
    score = random.randint(1, 10)

    if score < 5:
        print(f"当前第{i}个员工，绩效不够，不发工资。")
        continue

    if money >= 1000:
        money -= 1000
        print(f"当前第{i}个员工，满足条件，发工资1000元，下一位")
    else:
        print(f"公司账户余额不足，本月不发了，下个月再来")
        break
    