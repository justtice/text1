
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

print("----"*5+"魔法函数"+"----"*5)
# __init,__call__ ,__str__ 举例
class A():
    def __init__(self):
        print("我被调用了")

    def __call__(self, *args, **kwargs):
        print("我又被调用了again")

    def __str__(self):
        return "返回一个字符串"

    def __repr__(self):
        return "我不用使用print"
a =A()

a()  # 对象当函数调用的时候调用
print(a)
help(getattr)



## __setattr__案例

class P():
    def __init__(self):
        pass

    def __setattr__(self, key, value):
        print("设置属性 :{0}".format(key))
        # self.key = value   这句会造成死循环

        super().__setattr__(key,value)

p = P()
p.age = 18



## 运算类 __gt__

class Player():
    def __init__(self,name):
        self._name = name

    def __gt__(self,obj):
        print("哈哈,{0}会比{1}大吗?".format(self,obj))
        return self._name > obj._name

p1 = Player("ONE")
p2 = Player("two")
print(p1>p2)



#三种方法的案例

class Person():

    # 实例方法方法
    def eat(self):
        print(self)
        print("eating...")

    # 类方法
    @classmethod
    def play(cls):
        print(cls)
        print("playing...")

    #静态方法,不需要用第一个参数表示自身或类
    @staticmethod
    def say():
        print("saying")


p = Person()
#实例方法
p.eat()

# 对象也可以调用类方法,
p.play()
Person.play()

#静态方法  (不能修改,比如获取当前时间)

p.say()
Person.say()

print("*"*20)


## 类属性的property的应用场景
class A():
    def __init__(self):
        self.name= "网打哈"
        self.age = 18

    def fget(self):
        print("我被读取了")
        return self.name
    def fset(self,something):
        self.name = "图灵学院"+something

    def fdel(self):
        print("不能删除了")
        pass

    something = property(fget,fset,fdel,"这是说明文档")

a = A()
print(a.name)

print(a.something)
del a.something
a.something = "隔壁老王"
print(a.something)


print("抽象类,接口"+"*"*20)

#抽象类的实现
import abc

#声明一个类并且指定当前类的元类
class Human(metaclass=abc.ABCMeta):

    # 定义一个抽象方法
    @abc.abstractmethod
    def smoking(self):
        pass

    #定义类抽象方法
    @abc.abstractclassmethod
    def drink():
        pass

    #定义静态抽象方法
    @abc.abstractstaticmethod
    def play():
        pass



## 函数名可以当变量来用