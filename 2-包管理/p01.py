class Student():
    def __init__(self,name="隔壁老王",age=18):
        self.name = name
        self.age = age

    def say(self):
        print("my name is {0}".format(self.name))

def sayHello():
    print("hi,欢迎回家哦!")

# 直接运行这个文件的时候才会执行
# 准确的说每个模块的程序都是以这句话为入口
if __name__ == '__main__':

    print("我是模块01,你叫我干嘛")


