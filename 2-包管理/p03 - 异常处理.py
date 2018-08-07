
# 简单异常案例
try:
    num = int(input("输入你要的数字:"))
    rst = 100/num
    # print("计算结果:{0}".format(rst))

    print(100/num)

#捕获异常,把异常实例化,
except ZeroDivisionError as e:
    print("输入的什么玩意")
    print(e)

#所有异常都是exception的子类
except Exception as e:
    print("我也不知道就出错了")
    print(e)

print("哈哈哈")

print("*"*20)

## 用户手动引发一个异常
# raise 关键字来引发异常
#自定义异常, 必须是异常的子类
class DanaError(ValueError):
    pass
try:
    print("dawdaw")
    print("3.14")
    raise  DanaError
    print("nameerror")
except DanaError:
    print("danaError")



