#coding: utf-8

def main():
    n = 600851475143
    pos = 1
    while (n > 1):
        pos += 2
        while (n%pos == 0):
            n /= pos
    print(pos)

if __name__ == '__main__':
    main()
