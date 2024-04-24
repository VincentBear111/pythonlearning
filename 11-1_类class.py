class Student:
    # 属性
    name = None     # 学生姓名
    age = None      # 学生年龄

    # 方法
    def say_hi(self):
        print(f"大家好呀, 我是{self.name}, 我今年{self.age}岁了.")

# 实例化对象
stu = Student()
stu.name = "bear"
stu.age = 13
stu.say_hi()


class Cube:
    # python语言中类内调用私有成员和方法需要使用 self. 出来
    # 私有成员变量(定义:变量前面添加两个下划线)--外界不可调用
    __mW:int = None
    __mH:int = None
    __mL:int = None

    # 构造方法 -- 此处方法中既可以定义成员变量, 又可以对其进行赋值操作
    # __init__()方法中的是公共成员变量, 外界可调用
    # def __init__(self, _len, _width, _height):
    #     self.mLen = _len
    #     self.mWidth = _width
    #     self.mHeight = _height

    # 方法
    @property
    def getL(self):
        return self.__mL

    @getL.setter
    def setL(self, len):
        self.__mL = len
    
    def setW(self, width):
        self.__mW = width
    
    def getW(self):
        return self.__mW
    
    def setH(self, height):
        self.__mH = height

    def getH(self):
        return self.__mH
    
    # 公共成员方法(计算立方体的面积)
    def calcCubeArea(self):
        return (self.mLen * self.mWidth + self.mLen * self.mHeight + self.mHeight * self.mWidth)*2

    # 私有成员方法(计算面积)
    def __calcCubeArea(self):
        return (self.__mL * self.__mW + self.__mL * self.__mH + self.__mW * self.__mH)*2

    # 公共成员方法(计算立方体的体积)
    def calcVolumn(self):
        return self.mLen * self.mWidth * self.mHeight
    
    # 私有成员方法(计算体积)
    def __calcVolumn(self):
        return self.__mL * self.__mW * self.__mH

    def getArea(self):
        area = self.__calcCubeArea()
        return area
    
    def getVolumn(self):
        vol = self.__calcVolumn()
        return vol
    
print("================Cube1================")
cube1 = Cube()
cube1.setH(2.5)
cube1.setW(1.5)
cube1.setL(2)
print(f"长:{cube1.getL()}, 宽:{cube1.getW()}, 高:{cube1.getH()}")
area = cube1.getArea()
print(f"area : {area}")
volumn = cube1.getVolumn()
print(f"volumn : {volumn}")


"""
python的内置魔术方法:(用于两个类对象之间的比较运算)
1. __init__()
2. __str___()
3. __lt__()         # 完成两个类的小于或大于符号的比较
4. __le__()
5. __eq__()         # 比较运算符实现
"""
from typing import Union