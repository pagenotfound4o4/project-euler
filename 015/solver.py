#coding: utf-8

def C(n, m):
    ret = 1
    for i in range(n, n-m, -1):
        ret *= i
    for i in range(2, m+1):
        ret /= i
    return ret

def main():
    print(C(40, 20))

if __name__ == '__main__':
    main()
