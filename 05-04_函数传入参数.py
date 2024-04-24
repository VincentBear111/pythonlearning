if False:
    def add(x, y):
        if type(x) != type(y):
            print("x和y的类型不同，无法进行加法操作。")
            return
        
        return x + y

        print(add('1', '2'))

"""
函数说明文档：
    函数说明
    :param1 x: 形参x的说明
    :parma2 y: 形参y的说明
    :return  : 返回值的说明
"""

# global关键字可以将局部变量声明为全局变量


"""
函数综合案例
"""

money = 5000000
name = ''

def query(show_header):
    """
    查询余额函数
    """
    if show_header:
        print("-----------查询余额------------")
    print(f"{name}您好，您当前银行卡余额为{money}元。")

def saving(num):
    """
    存款函数
    """
    global money
    money += num
    print(f"{name}您好，您当前存款{num}元。")

    query(False)

def get_money(num):
    """
    取款函数
    """
    global money
    money -= num
    print(f"{name}您好，您当前取款{num}元。")

    query(False)

def main():
    print(f"{name}您好，欢迎来到黑马银行ATM，请您选择操作：")
    print("查询余额\t【输入1】")
    print("存款\t\t【输入2】")
    print("取款\t\t【输入3】")
    print("退出\t\t【输入4】")

name = input("请输入您的姓名：")
while True:
    main()

    operator = input("请输入您的操作选项：")
    if operator == '1':
        query(True)
        continue
    elif operator == '2':
        save_num = int(input("请您输入存款金额："))
        saving(save_num)
        continue
    elif operator == '3':
        _money = int(input("请您输入取款金额："))
        get_money(_money)
        continue
    else:
        print("程序退出，感谢您的使用")
        break