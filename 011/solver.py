#coding: utf-8

def get_max(arr, n, m, x, y):
    ret = 0
    # left to right
    if y + 4 <= m:
        tmp = reduce(lambda x, y: x * y, [arr[x][y+i] for i in range(4)])
        ret = max(ret, tmp)

    # up to down
    if x + 4 <= n:
        tmp = reduce(lambda x, y: x * y, [arr[x+i][y] for i in range(4)])
        ret = max(ret, tmp)

    # left-top to right down
    if x + 4 <= n and y + 4 <= m:
        tmp = reduce(lambda x, y: x * y, [arr[x+i][y+i] for i in range(4)])
        ret = max(ret, tmp)

    # right-top to left down
    if x + 4 <= n and y - 3 >= 0:
        tmp = reduce(lambda x, y: x * y, [arr[x+i][y-i] for i in range(4)])
        ret = max(ret, tmp)
    return ret

def product(arr, n, m):
    maxv = 0
    for i in range(n):
        for j in range(m):
            maxv = max(maxv, get_max(arr, n, m, i, j))
    return maxv

with open('in.txt', 'r') as fin:
    lines = [line.rstrip('\r\n') for line in fin.readlines()]
arr = list()
for line in lines:
    arr.append([int(item) for item in line.split()])
n , m = len(arr), len(arr[0])
print(product(arr, n, m))
