
class Person():
    # name是共有的成员
    name = "liuling"
    # __age 就是私有变量
    __age = 18


p = Person()
print(p.name)

#age 私有  (是个假私有, 就是改了个名)
print(p._Person__age)

print("*"*20)

##  继承的语法

class Person():
    name = "NoName"
    age = 18
    __score = 0  # 考试分数是私有的, 只有自己知道
    _petname = "sec" # 小名, 是保护的,子类可以用,da但不能公用
    def sleep(self):
        print("sleeping... ...")

    def work(self):
        print("make some money")

class Teacher(Person):
    teacher_id = 7758
    def make_test(self):
        print("teach student..")

    def work(self):
        #扩充父类的功能只需要调用父类相应的函数
        # Person.work(self)
        #调用父类的另一种方法
        super().work()
        self.make_test()

t = Teacher()
print(t.name)
#受保护的的
print(t._petname)
#私有的不能访问 t.__score
# t.sleep()

print("*"*25)
t.work()

print("*"*25)


#构造函数
class Animal():
    def __init__(self):
        print("animal..")


class paxingAni(Animal):
    def __init__(self,name):
        print("爬行动物的构造函数名字{0}".format(name))

class Dog(paxingAni):
    # __init__    就是构造函数
    # 每次实例化的时候第一个被调用的
    def __init__(self):
        print("i am a suger")


# 因为找到了构造函数, 所以不向上查找构造函数
suger = Dog()  # 初始化的时候就调用了__init__

suger = paxingAni("suger")  # 爬行动物的构造函数,带了name的参数

