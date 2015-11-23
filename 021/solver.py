#coding: utf-8
import math

dic = dict()

def d(n):
    ret = 1
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            ret += i
            if n / i != i:
                ret += n / i
    return ret

def is_amicable(n):
    if n in dic and dic[n] in dic:
        if dic[dic[n]] == n and dic[n] != n:
            return True
        return False
    dn = d(n)
    dnn = d(dn)
    dic[n] = dn
    dic[dn] = dnn
    return is_amicable(n)

n = 0
for i in range(1, 10001):
    if is_amicable(i):
        n += i
print(n)
