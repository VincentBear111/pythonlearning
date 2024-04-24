### 练习

# 练习1:定义一个类描述数字时钟
from time import sleep

class Clock(object):
    """
    数字时钟
    """

    def __init__(self, hour: int=0, min: int=0, sec: int=0) -> None:
        """
        初始化方法: 时 分 秒
        """
        self._hour = hour
        self._min = min
        self._sec = sec
    
    def run(self):
        """
        走字
        """
        self._sec += 1
        if self._sec == 60:
            self._sec = 0
            self._min += 1
            if self._min == 60:
                self._min = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0
    
    def show(self):
        """
        显示时间
        """
        return '%02d:%02d:%02d' % (self._hour, self._min, self._sec)


# def main():
#     clock = Clock(22, 15, 45)
#     while True:
#         print(clock.show())
#         sleep(1)
#         clock.run()

# if __name__ == '__main__':
#     main()
        

## 练习2: 定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法
from math import sqrt

class Point(object):

    def __init__(self, x: int=0, y: int=0) -> None:
        """初始化方法"""
        self._x = x
        self._y = y

    def move_to(self, x: float=0.0, y: float=0.0):
        """
        移动到指定位置的方法
        """
        self._x = x
        self._y = y
    
    def move_by(self, dx :float=0.0, dy: float=0.0):
        """
        移动到指定位置的增量
        """
        self._x = self._x + dx
        self._y = self._y + dy

    def distance_to(self, other):
        """
        计算与另一个点的距离
        """
        dx = self._x - other._x
        dy = self._y - other._y
        return sqrt(dx**2 + dy**2)
    
    def __str__(self) -> str:
        return '(%s, %s)' %(str(self._x), str(self._y))
    

# def main():
#     p1 = Point(3, 5)
#     p2 = Point()
#     print(p1)
#     print(p2)

#     p2.move_by(-1, 2)
#     print(p2)
#     print(p1.distance_to(p2))

# if __name__ == '__main__':
#     main()
    

class Person(object):

    def __init__(self, name: str='', age: int=0):
        """
        初始化方法(类似于c++中的构造函数)
        """
        self._name = name
        self._age = age

    # 访问器 - getter方法
    @property
    def name(self):
        return self._name
    
    # 修改器 - setter方法
    @name.setter
    def name(self, name):
        self._name = name

    # 访问器 - getter方法
    @property
    def age(self):
        return self._age
    
    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age < 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


# def main():
#     person = Person('王大锤', 12)
#     person.play()
#     person.age = 22
#     person.play()
#     person.name = 'bear'
#     person.play()

# if __name__ == '__main__':
#     main()
            

# 类中静态方法的使用
class Triangle(object):

    def __init__(self, a: float=0.0, b: float=1.0, c: float=2.0) -> None:
        self._a = a
        self._b = b
        self._c = c

    # 静态成员方法的使用:需要在创建对象之前调用的方法, 将其设计为静态方法
    @staticmethod
    def is_valid(a: float=0.0, b: float=1.0, c: float=2.0) -> bool:
        if (a + b > c) or (a + c > b) or (b + c > a):
            return True
        else:
            return False
    
    @property
    def a(self):
        return self._a
    
    @a.setter
    def a(self, a):
        self._a = a

    def perimeter(self):
        return self._a + self._b + self._c
    
    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) * (half - self._b) * (half - self._c))
    
def main():
    a, b, c = 3, 4, 5
    if Triangle.is_valid(a,b,c):
        t = Triangle(a,b,c)
        print(t.perimeter())
        print(t.area())
    else:
        print("无法构成三角形.")


##### 抽象类案例:
# 案例1: 奥特曼打小怪兽
from abc import ABCMeta, abstractmethod
from random import randint, randrange

class Fighter(object, metaclass=ABCMeta):
    """战斗者"""

    # 通过__slots__魔法限定对象可以绑定的成员变量
    __slots__ = ('_name', '_hp')

    def __init__(self, name: str='', hp: float=0.0) -> None:
        """
        初始化方法:
        :param name:    名字
        :param hp:      生命值
        """
        self._name = name
        self._hp = hp
    
    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp
    
    @hp.setter
    def hp(self, hp: float=0.0):
        self._hp = hp if hp >= 0 else 0
    
    @property
    def alive(self):
        return self._hp > 0

    # 抽象方法
    @abstractmethod
    def attack(self, other):
        """
        攻击:
        :param other: 被攻击的对象
        """
        pass


class Ultraman(Fighter):
    """
    奥特曼:
    """

    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name: str='', hp: float=0.0, mp: float=0.0) -> None:
        """
        初始化方法:
        :param name:     名字
        :param hp:      生命值
        :param mp:      魔法值
        """
        super().__init__(name=name, hp=hp)
        self._mp = mp
    
    def attack(self, other):
        other.hp -= randint(15, 25)

    def huge_attack(self, other):
        """
        究极必杀技(打掉对方至少50点或四分之三的血量)
        :param other:       被攻击的对象
        :return : 使用成功返回True否则返回False
        """
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True
        else:
            self.attack(other=other)
            return False
        
    def magic_attacks(self, others):
        """
        魔法攻击:
        :param others:      被攻击的群体
        :return: 使用魔法成功返回True否则返回False
        """
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(10, 15)
            return True
        else:
            return False
        
    def resume(self):
        """
        恢复魔法值
        """
        incr_point = randint(1, 10)
        self._mp += incr_point
        return incr_point
    
    def __str__(self) -> str:
        return '~~~%s奥特曼~~~\n' % self._name + \
            '生命值: %d\n' % self._hp + \
            '魔法值: %d\n' % self._mp
    
class Monster(Fighter):
    """
    小怪兽
    """

    __slots__ = ('_name', '_hp')

    def attack(self, other):
        other.hp -= randint(10, 20)
    
    def __str__(self) -> str:
        return '~~~%s~~~\n' % self._name + \
            '生命值: %d \n' % self._hp
    
def is_any_alive(monsters):
    """
    判断有没有小怪兽是活着的
    """
    for monster in monsters:
        if monster.alive > 0:
            return True
    return False

def select_alive_one(monsters):
    """
    选中一只活着的小怪兽
    """
    monsters_len = len(monsters)
    while True:
        idx = randrange(monsters_len)
        monster = monsters[idx]
        if monster.alive > 0:
            return monster
        
def display_info(ultraman, monsters):
    """
    显示奥特曼和小怪兽的信息
    """
    print(ultraman)
    for monster in monsters:
        print(monster, end=' ')

def main():
    u = Ultraman('骆昊', 1000, 120)
    m1 = Monster('狄仁杰', 250)
    m2 = Monster('白元芳', 500)
    m3 = Monster('王大锤', 750)
    ms = [m1, m2, m3]

    fight_round1 = 1
    while u.alive and is_any_alive(ms):
        print('=============第%02d回合==========' % fight_round1)
        m = select_alive_one(ms)        # 选中一只小怪兽
        skill = randint(1, 10)          # 通过随机数选择使用哪种技能
        if skill <= 6:                  # 60%的概率使用普通攻击
            print('%s使用普通攻击打了%s.' % (u.name, m.name))
            u.attack(m)
            print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
        elif skill <= 9:                # 30%的概率使用魔法攻击(可能因魔法值不足而失败)
            if u.magic_attacks(ms):
                print('%s使用了魔法攻击.' % u.name)
            else:
                print('%s使用魔法失败!' % u.name)
        else:                           # 10%的概率使用究极必杀技(如果魔法值不足就使用普通攻击)
            if u.huge_attack(m):
                print('%s使用究极必杀技虐了%s' % (u.name, m.name))
            else:
                print('%s使用普通攻击打了%s' % (u.name, m.name))
                print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
        
        if m.alive > 0:                 # 如果选中的小怪兽没有死就回击奥特曼
            print('%s回击了%s' % (m.name, u.name))
            m.attack(u)
        display_info(u, ms)             # 每个回合结束后显示奥特曼和小怪兽的信息
        fight_round1 += 1
    print('\n=========战斗结束!=======\n')

    if u.alive > 0:
        print('%s奥特曼胜利!' % u.name)
    else:
        print('小怪兽胜利!')


if __name__ == '__main__':
    main()