# 集合推导式    字典推导式
# 去重找到元素中>5的 然后+1
list1 = [1,1,2,2,6,6,7,7,78,9]
set1={i+1 for i in list1 if i>5}
print(set1)

#字典推导式
dict1={'a':'A','b':'B','c':'C','d':'D'}
#颠倒 key value
newdict={j:i for i,j in dict1.items()} #items()将dict转成tuple
print(newdict)