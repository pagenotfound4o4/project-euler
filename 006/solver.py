#coding: utf-8

def main():
    n1 = 0
    for i in range(1, 101):
        n1 += i ** 2
    n2 = (1 + 100) * 100 / 2
    n2 = n2 ** 2
    print(n2 - n1)
    pass

if __name__ == '__main__':
    main()
