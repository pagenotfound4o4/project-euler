#coding: utf-8
import math

def count(n):
    ret = 1
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            if n / i == i:
                ret += 1
            else:
                ret += 2
    if n > 1:
        ret += 1
    return ret

def main():
    total, n = 0, 1
    while True:
        total += n
        n += 1
        cnt = count(total)
        if cnt > 500:
            print(total)
            break

if __name__ == '__main__':
    main()
