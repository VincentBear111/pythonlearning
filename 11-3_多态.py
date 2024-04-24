class Animal:
    # 方法体是空实现的就是抽象方法, 该类就是抽象类
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("我是小狗,汪汪汪...")

class Cat(Animal):
    def speak(self):
        print("我是小猫,喵喵喵...")

# 生命方法时将父类当做形参传入, 调用方法时传入子类的对象, 形成多态
def doSpeak(animal: Animal):
    animal.speak()


dog = Dog()
cat = Cat()
# 调用do_speak方法
doSpeak(dog)
doSpeak(cat)