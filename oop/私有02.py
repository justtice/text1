
class Person():
    # name是共有的成员
    name = "liuling"
    # __age 就是私有变量
    __age = 18


p = Person()
print(p.name)

#age 私有  (是个假私有, 就是改了个名)
print(p._Person__age)


