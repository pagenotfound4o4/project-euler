#coding: utf-8

def isPal(n):
    s = str(n)
    for i in range(len(s)/2):
        if s[i] != s[len(s)-i-1]:
            return False
    return True

def main():
    maxv = 0
    for i in range(1000):
        for j in range(1000):
            if isPal(i*j):
                maxv = max(maxv, i*j)
    print(maxv)

if __name__ == '__main__':
    main()
