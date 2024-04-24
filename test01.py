import  torch
import torchvision
import onnx
import onnxruntime
from matplotlib import pyplot as plt
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt


# print("hello python")
# print(torch.__version__)
# print(torch.cuda.is_available())

# print('-'*40)


# 练习一:华氏温度转换为摄氏温度
# f = float(input("请输入华氏温度:"))
# c = (f - 32) / 1.8
# print("%.1f华氏度 = %.1f摄氏度" % (f, c))

# 练习二:输入圆的半径计算圆的周长和面积
# r = float(input('请输入圆的半径:'))
# perimeter = 2 * 3.1415926 * r
# area = 3.1415926 * r * r
# print('周长: %.2f' % perimeter)
# print('面积: %.2f' % area)

# 练习三:输入年份判断是不是闰年
# year = int(input("请输入一个年份:"))
# is_leap = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
# if is_leap:
#     print('您输入的年份%d年是闰年!' % year)
# else:
#     print('您输入的年份%d年不是闰年!' % year)

# 输入一个正整数并判断它是不是素数
# from math import sqrt

# num = int(input('请输入一个正整数:'))
# end = int(sqrt(num))
# is_prime = True
# for x in range(2, end + 1):
#     if num % x == 0:
#         is_prime = False
#         break

# if is_prime and num != 1:
#     print('%d是素数.' % num)
# else:
#     print('%d不是素数.' % num)

# for x in range(0, 20):
#     for y in range(0, 33):
#         z = 100 - x - y
#         if 5 * x + 3 * y + z / 3 == 100:
#             print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))

# fruits = ['grape', 'apple', 'strawberry', 'waxberry']
# fruits += ['pitaya', 'pear', 'mango']
# print(fruits)
# print('-' * 50)

# list1 = sorted(fruits)
# print(list1)
# print('-' * 50)
# print(fruits)


import os
import time
import random
def main():
    content = '北京欢迎你为你开天辟地…………'
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]

# 生成指定长度的验证码函数
def generate_code(code_len=6):
    all_chars = '0123456789abcdefghigklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    
    return code

# 获取文件名的后缀名
def get_suffix(filename: str, has_dot=False):
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''

# 获取列表中最大的两个值
def get_max_two_value(x: list):
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])

    for idx in range(2, len(x)):
        if x[idx] > m1:
            m2 = m1
            m1 = x[idx]            
        elif x[idx] > m2:
            m2 = x[idx]
    return m1, m2

def print_yh_triangle(rows: int):
    yh = [[]] * rows
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col] ,end='\t')
        print()


# 双色球选号案例
from random import randrange, randint, sample

def display(balls: list):
    """
    输出列表中的双色球号码
    """
    for idx, ball in enumerate(balls):
        if idx == len(balls) - 1: 
            print('|', end=' ')
        print('%02d' % ball, end=' ')
    print()

def random_select():
    """
    随机选择一组号码
    """
    red_balls = [x for x in range(1, 34)]
    select_balls = []
    select_balls = sample(red_balls, 6)
    select_balls.sort()
    select_balls.append(randint(1, 16))
    return select_balls

def main():
    count = int(input('机选几注:'))
    for _ in range(count):
        display(random_select())


def lucky_christian():
    persons = [True] * 30
    count, idx, number = 0, 0, 0
    while count < 15:
        if persons[idx]:
            number += 1
            if number == 9:
                persons[idx] = False
                count += 1
                number = 0
        idx += 1
        idx = idx % 30           # %= 取摸运算
        print(idx)
    for person in persons:
        print('基督徒' if person else '非基督徒', end=' ')

if __name__ == '__main__':
    # suffix = get_suffix('H:\PythonLearning\.idea')
    # print(suffix)
    # print('-'*50)
    # x = [11,12,3,2,6,5,9,8,7,10]
    # v1, v2 = get_max_two_value(x)
    # print('v1:%d, v2:%d' % (v1, v2))
    # print('-'*50)
    # print_yh_triangle(10)
    # print(randint(1, 16))    
    # main()
    lucky_christian()