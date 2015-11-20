#coding: utf-8

def main():
    with open('in.txt', 'r') as fin:
        s = "".join([line.rstrip('\r\n') for line in fin.readlines()])
    maxv = 0
    for start in range(len(s)-13):
        tmp = 1
        for shift in range(13):
            tmp *= int(s[start+shift])
        maxv = max(maxv, tmp)
    print(maxv)

if __name__ == '__main__':
    main()
