
'''
定义一个学生类
'''

class Student():
    pass




#定义一个对象
mingyue = Student()


# 在定义一个听python的学生类

class PythonStudent():
    name = None
    age = 18
    course = "python"

    def doHomeWork(self):
        print("在做作用")
        return  None


liuliu = PythonStudent()
liuliu.age  = 28
liuliu.name = "liuliu"
liuliu.doHomeWork()
print(liuliu.age,liuliu.name)

print(liuliu.__dict__)
print(PythonStudent.__dict__)



# 调用绑定类的参数, 没有self
class Teacher():
    name = "wowo"
    age = 18
    #self 不是关键字 , 随便用一个变量都可以代替
    def say(self):
        self.name  ="琉璃"
        self.age = 17
        print("my name is {0}".format(self.name))
        print("my age is {0}".format(self.age))

    def sayAgain():
        # 调用类的属性,用__class__
        print(__class__.name)
        print(__class__.age)
        print("nice to see you again")

t = Teacher()
t.say()
#调用的绑定类的函数,使用类名
Teacher.sayAgain()


# python 里没有强类型检测
class A():
    name = "琉璃"
    age = 17

    #构造函数
    def __init__(self):
        self.name = "aaa"
        self.age = 200

    def say(self):
        print("my name is {0}".format(self.name))
        print("my age is {0}".format(self.age))

class B():
    name = "lili"
    age = 90

a = A()
#此时,系统会默认把a作为第一个参数传入函数
a.say()

#此时self 被 a 替换
A.say(a)     #my name is aaa my age is 200
#此时,self 被 A 替换
A.say(A)     # my name is 琉璃   my age is 17

# 此时, 传入类实例B ,因为B具有name和agesh属性,所以不会报错, python 没有强类型检测
A.say(B)

