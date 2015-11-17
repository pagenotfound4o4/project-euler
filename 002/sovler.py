#coding: utf-8

def main():
    a = [1, 2, 0]
    sum = 2
    while (a[1] <= 4000000):
        a[2] = a[0] + a[1]
        a[0] = a[1]
        a[1] = a[2]
        if a[1] % 2 == 0:
            sum += a[1]
    print(sum)

if __name__ == '__main__':
    main()
