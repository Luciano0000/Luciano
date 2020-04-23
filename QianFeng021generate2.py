'''
生成器方法:
.__next__(): 获取下一个元素
.send(value) 向每次生成器调用中传值 注意: 第一次调用必须要调用send(None)
'''


def gen():
    i = 0
    while i < 5:
        temp = yield i #程序第一次运行 yield不传任何值 temp 是空 
        print(temp)
        i += 1
    return '没有更多的数据!'


g = gen()
# print(next(g))
# print(next(g))
# print(next(g))
# g.__next__()
print('num', g.send(None)) #由于 temp第一次运行位空,所以要生成一个None来传给temp
print(g.send('num 1'))
print(g.send('num 2'))

# 生成器的应用: 协程  (进程>线程>协程)
# 迅雷下载:


def task1(n):
    for i in range(n):
        print('正在解决第{}计算机线程拥堵问题'.format(i))
        yield None


def task2(n):
    for i in range(n):
        print('正在解决第{}网络拥堵问题'.format(i))
        yield None


g1 = task1(10)
g2 = task2(5)

while True:
    try:
        g1.__next__()
        g2.__next__()
    except:
        print('网络拥堵已解决推出双进程.')
        break
