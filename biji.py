(代码换行，实际不换行)
# total='appalPrice'\
#       +'bananaPrice'\
#       +'pearPrice'
# print(total)
#
# appalPrice=1; bananaPrice=2; pearPrice=3
# a=(appalPrice+bananaPrice+pearPrice)
# print(a)
#
# import keyword
# print(keyword.iskeyword('admin'))
#
# print(keyword.kwlist)
#
# x = 4
# y = x
# print(x,id(x))
# print(y,id(y))
# x = 5
# print(x,id(x))
# print(y,id(y))
#
# a = [1,2,'hello']  #列表
# a = {'name':'123','age':18}  #字典
#
# print(int(3.14))    #非四舍五入
# print(int(0.2))     #浮点数转换成整数类型
#
# print(int(True))
# print(int(False))
# print(bool(1))
# print(bool(2))
# print(bool(5))
# print(bool(5.5))
# print(bo('helloworld'))
# # print(bool(''))    #无值是显示False
# print(bool(' '))   #空格也算值
#
# a = "Apple's unit price is 9 yuan"
# #    0123456789
# print(a[22]) #第22位
# print(a[-6])
# print(a[13:18]) #13位到18位
# print(a[1:100]) #截取1至100位
# print(a[:100]) #从头开始截取
#
# 拼接
# print('456'+'123')
# print('456''123')
# print('456','123')
# print('456'+'123'*4)
#
# #修改
# a = "Apple's unit price is 9 yuan"
# #将9改为6，切片法
# b = a[0:22]
# c = a[23:28]
# print(b+'6'+c)
#
# a = 'Apple\'s unit price is 9 yuan'
# b =(a[22])
# print(type(b))
# b = int(b)
# print(b)
#
# print('1'=='2')
# print('2'>'1')
# print('a'<'b')
# print('b'<'a')
#
# print(ord('a')) #将字母转换成ASCII字符
# print(ord('b'))
# print(chr(97)) #将ASCII字符转换成对应的字母
# print(chr(98))
#
# print(bin(a))  #bin函数用来将十进制书转换成二进制数
#
# print(a and b)  #顺序查找false的值，找到则输出false，如果没有找到，则输出最后一个值
#
# List = [1,2,3,4,[5,6],'123']
# print(1 in List) #判断元素1是否存在于字典List中
#
# r = input('r=')
# r = int(r)
# c = 2*3.14*r
# print('周长=',c)
#
# s = r**2*3.14
# print('面积=',s)
#
# s = input('s=')
# s = int(s)
# r = (s/3.14)**0.5
# l = 2*s/r
# print('半径=',r)
# print('周长=',l)
#
# print(round((s/3.14)**0.5))
# print(round((2*s/r))
#
#
# x = int(input('请输入第一个数字:'))
# y = int(input('请输入第二个数字:'))
# z = int(input('请输入第三个数字:'))
# m = 3
# u = (x+y+z)/m
# u = int(u)
# print('均值=',u)
# f = (((x-u)**2+(y-u)**2+(z-u)**2)/m)
# f = int(f)
# print('方差=',f)
# b = f**(1/2)
# b = int(b)
# print('标准差=',b)
#
# x = float(input('请输入第一个数字:'))
# y = float(input('请输入第二个数字:'))
# z = float(input('请输入第三个数字:'))
# m = 3
# u = (x+y+z)/m
# u = float(u)
# print('均值 =',u)
# f = (((x-u)**2+(y-u)**2+(z-u)**2)/m)
# f = float(f)
# print('方差 =',f)
# b = f**(1/2)
# b = float(b)
# print('标准差 =',b)
#
# ccc = [1,2,[1,2,3],4,5,6]
# print(ccc[0:4:2])   #1为步长，隔0取数。如果2为步长，隔1取数
# print(ccc[5:0:-1])   #倒过来
#
# a = [110,'dog','cat',120, 'apple']
# print(a)
# (a.insert(2,[]))
# (a.remove('apple'))
# a[0]=a[0]*10
# a[4]=a[4]*10
# print(a)
#
# a = [110,'dog','cat',120, 'apple']
# print(a.index(120)) #查询120在列表的那个位置
#
# #copy
# a = [1,2,3]
# b = a.copy()
# print(a,id(a))  #a,b地址不相同
# print(b,id(b))
#
# # 不可变数据类型(数值,字符串,元组)
# a = 1
# b = a
# print(a,id(a))  #a,b地址相同
# print(b,id(b))
# # 可变数据类型(列表)
# a = [1,2,3]
# b = a
# a[2] = 300
# print(a,id(a))  #a,b地址不相同
# print(b,id(b))
#
# #copy
# a = [1,2,3]
# b = a.copy()
# c = a[:]
# d = list(a)
# print(a,id(a))
# print(b,id(b))
# print(c,id(c))
# print(d,id(d))
# #b,c,d地址都不同于a
#
#
# a = [1,2,3,4,5,6,2,2,2]
# print(a.count(2))  #查询2在list(a)中出现了几次
#
# a = [1,2,3,4,5,6,2,2,2]
# a.sort()     #排序，默认从小到大(False)
# print(a)
# a.sort(reverse= True)  #True代表降序
# print(a)
# a.sort(reverse= False) #False代表升序
# print(a)
#
# a = [1,2,3,4,5,6,2,2,2]
# print(sorted(a)) #已改变
# print(a) #但a本身没有改变
#
# a = [1,2,3,4,5,6,2,2,2]
# print(a)
# a.reverse()  #将列表倒过来
# print(a)
#
# a = ['123',1,2,3]
# print(len(a)) #数a中有几个元素
#
# a = (1,2,3)
# b = tuple([1,2,3])  #将list(a)转换成tuple(a),元组的创建,元组不可改变
# print(a)
# print(b)
# print(a[0:2])       #可切片
#
# a = (1,2,3)
# A,B,C = a  #a与A对应
# print(A)
#
#
# a = {'x':1,'y':2,'z':3}
# print('x' in a)
# print('e' in a)
#
# print(a.get('x'))
# print(a.get('y'))
#
# print(a.get('x',3))   #存在输出存在的值x，不存在输出3
# print(a.get('j',4))   #存在输出存在的值j，不存在输出4
#
# a['新增'] = 5
# print(a)
#
# #拼接
# a = {'x':1,'y':2,'z':3}
# b = {'q':4,'w':5,'e':6}
# a.update(b)
# print(a)
#
# a = {'x':1,'y':2,'z':3}
# b = {'x':4,'y':5,'z':6}
# a.update(b)   #重复的会被后者取代
# print(a)
#
# a = {'x':1,'y':2,'z':3}
# del a['x']
# print(a)
# a.pop('y')
# print(a)
# a.clear()   #清空字典
# print(a)
#
# #修改
# a = {'x':1,'y':2,'z':3}
# a['x'] = 4
# print(a)
#
# b = a.keys()  #获取全部键
# print(b)
# c = a.values()   #获取全部值
# print(c)
# d = a.items()   #获取全部内容
# print(d)
#
#
# p68
# a = {'Math':96,'English':86,'Chinese':95.5,'Biology':86,'Physics':None}
# b = {'History':88}
# a.update(b)
# print(a)
# del a['Physics']
# print(a)
# a['Chinese'] = round(a['Chinese'])
# print(a)
# print(a.get('Math'))
#
# a = set([4,5,3,1,2])
# print(a)
# b = frozenset([4,5,3,1,2])
# print(b)
#
# a = {1,2,3,4,5}
# b = {4,5,6,7,8}
# # 并集
# print(a | b)
# print(a.union(b))
# #交集
# print(a & b)
# #差集
# print(a - b)
# print(b - a)
# print(a.difference(b))
# print(b.difference(a))
# #异或
# # a | b 去掉 a & b
# print(a ^ b)
# print(a.symmetric_difference(b))
# # <=  in   子集
# print(b <= a)   #子集
# print(b < a)    #真子集
# #超集
# print(a >= b)  #超集
# print(a > b)   #真超集
#
# a = {1,2,3,4,5}
# a.add(7)   #新增元素
# print(a)
#
# a.pop()   #删除元素
# print(a)
#
# a = ['apple','pear','watermelon','prach']
# b = ['pear','banana','orange','peach','grape']
# c = set(a)
# d = set(b)
# print(c | d)
# print(c & d)
# print(c - d)
#
# print('请选择需要进行操作的对应数字')
# print('查询汉堡类菜单请输入:1')
# print('查询小食类菜单请输入:2')
# print('查询饮料类菜单请输入:3')
# print('若不查询请输入:0')
# x = int(input('请输入数字:'))
# a = ('香辣鸡腿堡','劲脆鸡腿堡','奥尔良烤鸡腿堡','半鸡半虾堡')
# b = ('薯条','黄金鸡块','香甜栗米棒')
# c = ('可口可乐','九珍果汁','经典咖啡')
# d = ('感谢你的使用')
# if x == 1:
#     print(a)
# if x == 2:
#     print(b)
# if x == 3:
#     print(c)
# if x == 0:
#     print(d)
#
# import random （该函数可以取一个随机数字给变量）
# b=random.randint(0,10)
