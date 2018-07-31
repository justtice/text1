class Fish():
    def __init__(self,name):
        self.name = name
    def swim(self):
        print("swiming... ...")

class Bird():
    def __init__(self,name):
        self.name = name
    def fly(self):
        print('i am filing.. ..')

class Person():
    def __init__(self,name):
        self.name = name
    def work(self):
        print("make money..")

class SuperMan(Person,Bird,Fish):
    pass

s = SuperMan("超人")
s.work()
s.swim()
s.fly()


