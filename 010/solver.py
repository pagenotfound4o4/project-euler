#coding: utf-8

def main():
    max_num = 2000001
    vis = [True] * max_num
    for i in range(2, max_num):
        if vis[i]:
            j = 2
            while i*j < max_num:
                vis[i*j] = False
                j += 1
    total = 0
    for i in range(2, max_num):
        if vis[i]:
            total += i
    print(total)

if __name__ == '__main__':
    main()
