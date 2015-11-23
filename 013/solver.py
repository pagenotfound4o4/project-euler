#coding: utf-8

def main():
    with open('in.txt', 'r') as fin:
        lines = [line.rstrip('\r\n') for line in fin.readlines()]
    total = sum([int(item) for item in lines])
    print(str(total)[0:10])

if __name__ == '__main__':
    main()
