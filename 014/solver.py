#coding: utf-8


cnt = {1: 1}

def count(n):
    if n in cnt:
        return cnt[n]
    if n % 2 == 0:
        cnt[n] = count(n/2) + 1
    else:
        cnt[n] = count(3*n+1) + 1
    return cnt[n]

def main():
    max_num = 1000001
    maxp = 1
    for i in range(2, max_num):
        if count(i) > cnt[maxp]:
            maxp = i
    print(maxp)

if __name__ == '__main__':
    main()
