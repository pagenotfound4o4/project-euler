#coding: utf-8

n = reduce(lambda x, y: x * y, [i+1 for i in range(100)])
total = sum(int(c)-int('0') for c in str(n))
print(total)
