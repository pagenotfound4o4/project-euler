#coding: utf-8

def main():
    sum = 1000
    for a in range(1, 500):
        for b in range(a+1, 1000):
            c = sum - a - b
            if c <= b:
                break
            if a**2 + b**2 == c**2:
                print(a*b*c)

if __name__ == '__main__':
    main()
