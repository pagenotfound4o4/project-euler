#coding: utf-8

def main():
    max_num = 1000000
    vis = [True] * max_num
    for i in range(2, max_num):
        if vis[i]:
            j = 2
            while i*j<max_num:
                vis[i*j] = False
                j += 1
    cnt = 0
    for i in range(2, max_num):
        if vis[i]:
            cnt += 1
            if cnt == 10001:
                print(i)
                break

if __name__ == '__main__':
    main()
