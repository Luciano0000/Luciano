# 列表推导式  字典推导式  集合推导式
# 旧的列表--->新的列表


# 列表推导式:
# 格式:   [符合后面条件的表达式 for 变量 in  旧列表] 或者
# [符合后面条件的表达式 for 变量 in  旧列表 if 条件]
# 相当于 for 变量 in range()/列表:
#               if 条件句:
# 然后符合遍历和条件句的表达式传给新列表

# [[1,2,3],[4,5,6],[7,8,9],[1,3,5]]--->要得出一个[3,6,9,5]
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 3, 5]]
newlist = [i[-1] for i in list1]
print(newlist)


# 过滤掉长度< 或者 =3 的人名
names = ['tom', 'lucy', 'jack', 'steaven', 'bobs', 'ha']
result = [name for name in names if len(name) > 3]
print('利用列表推导', result)

# 过滤掉长度< 或者 =3 的人名 且第一个首字母大写
result = [name.capitalize() for name in names if len(name) > 3]
print('利用列表推导', result)
# 等价与上式(麻烦)


def func(names):
    newlist = []
    for name in names:
        if len(name) > 3:
            name = name.title()
            newlist.append(name)
    return newlist


x = func(names)
print('利用函数', x)

# 将1-100之间能够被三,五整除的,组成一个新的列表
newlist = [i for i in range(1, 101) if i % 3 == 0 and i % 5 == 0]
print(newlist)


# 0-5的偶数 0-10的奇数
# 将[(偶数,奇数),(),()]    [(0,1),(0,3),(0,5),(0,7),(0,9),(2,1),()....]

newlist = [(x, y) for x in range(5) if x %
           2 == 0 for y in range(10) if y % 2 != 0]
print(newlist)

# 等价上式(麻烦)


def func1():
    newlist = []
    for i in range(5):  # 偶数
        if i % 2 == 0:
            for j in range(10):  # 奇数
                if j % 2 != 0:
                    newlist.append((i, j))
    return newlist


a = func1()
print(a)


# 如果薪资大于5000加工资+200,低于等于5000加工资+500
dict1 = {'name': 'tom', 'salary': '8000'}
dict2 = {'name': 'jack', 'salary': '6000'}
dict3 = {'name': 'lucy', 'salary': '5000'}
dict4 = {'name': 'kam', 'salary': '15000'}

list2 = [dict1, dict2, dict3, dict4]

newlist = [employee['sqlary']+200 if employee['salary'] >
           5000 else employee['salary']+200 for employee in list2]
