#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

# 输入 + 判断
s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')

# 求偶数和
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

# 求平方根
def quadratic(a, b, c):
    derta = b*b - 4*a*c
    if(derta < 0):
        return None
    else:
        return ((-b + math.sqrt(derta)) / 2*a), ((-b - math.sqrt(derta)) / 2*a)

# 参数类型(args: tuple, kw: dict)
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

# 可变参数
def product(*args):
    n = 0
    pro = 1
    while n < len(args):
        pro = pro*args[n]
        n = n + 1
    return pro

# 递归(带 n * fact(n-1) 表达式会造成栈溢出)
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

# 尾递归优化( python 未做优化，还是会栈溢出 )
def fact(n):
    return fact_in(n, 1)

def fact_in(num, product):
    if num == 1:
        return product
    return fact_in(num - 1, product * num)

# 汉诺塔( 将 a 柱子上的 n 个盘子移动到 c )
def move(n, a, buffer, c):
    if n == 1:
        print(a, '-->', c)
    else:
        # 将 a 之上 n-1 个通过 空c 移动到 buffer
        move(n - 1, a, c, buffer)
        # 将 a 上 最大一个 通过 buffer 移动到 c
        move(1, a, buffer, c)
        # 将 buffer 之上 n-1 个通过 空a 移动到 c
        move(n - 1, buffer, a, c)

# 用 slice 完成 trim
def trim(s):
    while s[0] == ' ':
        s = s[1:]
    while s[-1] == ' ':
        s = s[:-1]
    return s

# 用 for in 寻找最大最小值
def findMinAndMax(list):
    max = list[0]
    min = list[0]
    for num in list:
        if max < num:
            max = num
        if min > num:
            min = num
    return (min, max)

# 循环列表使字符串变为小写
def lowerStr(list):
    return [item.lower() for item in list if isinstance(item, str)] # 过滤其余值
    # newList = [] # 不过滤其余值
    # for item in list:
    #     if isinstance(item, str):
    #         item = item.lower()
    #     newList.append(item)
    # return newList

# generator 生成费布拉切数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield(b)
        a, b = b, a+b
        n = n + 1
    return 'done'

g = fib(6)
while True:
    try:
        print('g: ', next(g))
    except StopIteration as e:
        print('Generator return value', e.value)
        break

# 杨辉三角
def triangles(maxLen):
    L = [1]
    while len(L) <= maxLen:
        yield(L)
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))] # 补零后 相邻两位相加得下一 list
Ls = triangles(5)
for L in Ls:
    print(L)

# str to float
from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2float(str):
    def char2num(s):
        return DIGITS[s]
    sA = str.split('.')
    return reduce(lambda x,y: x * 10 + y, map(char2num, sA[0])) + reduce(lambda x,y: x / 10 + y, map(char2num, sA[1][::-1])) / 10

# filter 筛选素数
# 定义 odd generator
def _odd_numbers():
    n = 1
    while True:
        n = n + 2
        yield n

# 定义 素数筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0

# 结合 生成和筛选
def primes():
    yield 2
    item = _odd_numbers()
    while True:
        n = next(item)
        yield n
        item = filter(_not_divisible(n), item)

# 打印 1000 内的素数
for n in primes():
    if n < 1000:
        print(n)
    else:
        break


# 回数筛选
def _numbers():
    n = 100
    while True:
        n = n + 1
        yield n

def _test(n):
    # s = str(n)
    # length = len(s)
    # n = 0
    # while n < length:
    #     if s[n] != s[length - n - 1]:
    #         return False
    #     else:
    #         n = n + 1
    # return True
    return str(n) == str(n)[::-1] # 颠倒顺序比较

def _backNums():
    item = _numbers()
    while True:
        n = next(item)
        yield n
        item = filter(_test, item)

# 打印 1000 内的素数
for n in _backNums():
    if n < 1000:
        print(n)
    else:
        break

# sorted
sorted([36, 5, -4, 0, 7, -7], key=abs, reverse=True)

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def getName(item):
    return item[0]

sorted(L, key=getName)

# 闭包
def countCreater():
    n = 0
    def counter():
        nonlocal n # !!! list 作为全局变量不需特殊声明 普通变量必须声明
        n = n + 1
        return n
    return counter

counter = countCreater()

# 匿名函数 lambda 表达式
L = list(filter(lambda x: x % 2 == 1, range(1, 20)))

# 装饰器函数
import functools
def log(func):
    @functools.wraps(func) # 继承 func 的 __name__ 属性到 wrapper
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2018-1-23')

# 偏函数 设置函数默认参数 并返回新函数 且默认参数后期也可手动指定值
import functools
int2 = functools.partial(int, base=2)
int2('1000000') # 64
int2('1000000', base=10) # 1000000
