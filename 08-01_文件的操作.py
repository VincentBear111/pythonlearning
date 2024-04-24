"""
计算机中有许多可用的编码(翻译规则不同):
1. UTF-8    -- 类似通用编码格式(默认选择)
2. GBK
3. Big5 -- 繁体字常用等
"""

"""
文件的读取操作:打开, 读取, 写入, 关闭等操作;
"""

"""
打开文件函数: open()函数
在python中,使用open函数可以打开一个已经存在的文件,或者创建一个新文件
open(name, mode, encoding)
参数name: 是要打开的目标文件名的字符串(可以包含文件所在的具体路径);
参数mode: 设置打开文件的模式(访问模式): 只读, 写入, 追加等;
参数encoding: 编码格式(推荐使用UTF-8);

mdoe常用的三种基础访问模式:
'r' : 以只读的方式打开文件. 文件的指针将会放在文件的开头. 这是默认模式
'w' : 打开一个文件只用于写入. 如果该文件已经存在则打开文件, 并从头开始编辑, 原有内容会被删除
      如果该文件不存在, 就创建新文件
'a' : 打开一个文件用于追加. 如果该文件已存在, 新的内容将会被写入到已有内容之后.
      如果该文件不存在, 则创建文件夹进行写入

读操作相关方法:
** read()方法 : 文件对象.read(num)
num表示要从文件中读取的数据的长度(单位是字节), 如果没有传入num, 那么就表示读取文件的所有数据
** readlines()方法 : 
readlines可以按照行的方式把整个文件的内容进行一次性读取, 并且返回的是一个列表,其中每一行的数据为一个元素

"""
import os
f = open("测试.txt", 'r', encoding='UTF-8')
print(type(f))

# firstline = f.read(10)      # 读取10个字节
# firstline = f.read()        # 读取文件全部内容
# firstline = f.readline()    # 读取一行的内容
# firstline = f.readlines()   # 读取文件所有内容, 并将每行按照列表的形式存在一个列表中
# print(firstline)
# print(type(firstline))

# for循环遍历文件
for line in f:
    print(line)

# 文件的关闭
f.close()

# with open 语句
# with open("测试.txt", "r", encoding="UTF-8") as f:
#     for line in f:
#         print(f"每一行的数据:{line}")


"""
文件的写入操作:
注意: 
    *1. 直接调用write, 内容并没有真正写入文件, 而是会积攒在程序的内存中, 称之为缓冲区;
    *2. 当调用flush的时候, 内容才会被真正的写入文件;
    *3. 这样做是避免频繁的操作硬盘, 导致效率下降(攒一堆, 一次性写入磁盘)
"""
with open("测试.txt", "w", encoding="UTF-8") as f:
    f.write("你好, 传智播客\n")
    f.write("hello world\n")
    f.write("hello python")
    f.flush()

# with open 语句
with open("测试.txt", "r", encoding="UTF-8") as f:
    for line in f:
        print(f"每一行的数据:{line}")