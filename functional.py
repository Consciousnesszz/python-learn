# 函数式编程
def f(x):
    return x * x

r = map(f, [1,2,3])
print(list(r))

from functools import reduce
def fn(x, y):
    return x * 10 + y

reduce(fn, [1,2,3])

def char2num(s):
    digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    return digits[s]

reduce(fn, map(char2num, '112358')) # str 为可迭代对象

def normalize(list):
    def normal(word):
        return word[0].upper() + word[1:].lower()
    return map(normal, list)