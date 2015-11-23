#coding: utf-8

a = [1, 1, 2]
cnt = 3
while len(str(a[2])) < 1000:
    a[0] = a[1]
    a[1] = a[2]
    a[2] = a[0] + a[1]
    cnt += 1
print(cnt)
