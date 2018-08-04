def foo():
    print("你好")

foo()

s = 1
print(type(s))

#打印学生列表名字
l = ["zhangsan","lisi","wangwu","zhaol"]
for name in l:
    print(*name)


def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1

    return fib(n - 1) + fib(n - 2)


print(fib(35))