# generate 生成   generator生成器
# 节省内存 
'''
通过列表生成式(列表推导式),我们可以直接创建一个列表,但是,收到内存限制,列表容量肯定是有限的
而且,创建一个包含100万个元素的列表,不仅占用很大的存储空间
如果我们仅仅需要访问前面几个元素,后面的绝大多数元素的占用的空间都白白浪费了
所以,如果列表的元素可以按照某种算法推算出来,那我们是否可以在循环的过程中不断的推算
后续的元素呢?
这样就不必创建完整的List,从而节省大量的空间,在python中,这种一边循环一边计算的机制
称为:生成器(generator)

'''
# 只要函数中出现了yield 关键字,说明函数就不是函数了,是生成器
'''
生成器的两种获取方式:
 1.通过列表列表推导式得到生成器
 2.通过函数 和 yeild'''

'''
步骤
 1定义一个函数,函数中使用yeild    -->def func():
                                    .... 
               -->                      yeild .. 或者 temp=yeild ..
 2.调用函数,接收调用的结果      
 3.得到的结果就是生成器---->         g=func()
 4.借助与 next( g) 或者 g.__next__() 或者 g.send(value)产生元素,若元素产生完毕还继续调用则会出现异常''' 






g = (i*3 for i in range(10))  # ()
print(type(g))  # <class 'generator'>
print(g)  # <generator object <genexpr> at 0x02C8B4C0>


# 方式一:通过调用g.__next()__ 方式得到元素
# 调用一次next()会产生一个元素
'''
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
'''
# 方式二: next(生成器对象) 系统自带的内置函数
# 调用一次next()会产生一个元素
'''
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
'''
# print(next(g)) #Error: StopIteration 超出生成器本来可以产生的值的数量

while True:
    try:
        e = next(g)
        print(e)
    except:
        print('元素产生完毕,没有更多的元素了')
        print('利用try来控制生成器溢出问题')
        break


# 生成器:
def func():
    n = 0
    while True:
        n += 1
        yield n  # yeild相当于有暂停功能的return n


y = func()
print(y)
next(y)  # <generator object func at 0x03455E60> 这时已经开辟了一个内存存放第一个元素了
print(next(y))  # 2
print(next(y))  # 3


# 斐波那契数列0 1 1 2 3 5 8 13...

def fib(length):
    a, b = 0, 1
    n = 0

    while n < length:
        # print('b:', b)
        yield a,b
        a, b = b, a+b
        n += 1

    return '没有更多的元素' #元素迭代之后的错误信息: StopIteration: 没有更多的元素


g= fib(8)
for i in range(9):
    print(next(g))




