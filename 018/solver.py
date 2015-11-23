#coding: utf-8

arr, dp = [], []
with open('in.txt', 'r') as fin:
    lines = [line.rstrip("\r\n") for line in fin.readlines()]
for line in lines:
    arr.append([int(item) for item in line.split()])
    dp.append([0] * len(arr[-1]))
n = len(arr)
for i in range(n):
    dp[n-1][i] = arr[n-1][i]
for i in range(n-2, -1, -1):
    for j in range(i+1):
        dp[i][j] = max(dp[i+1][j], dp[i+1][j+1]) + arr[i][j]
print(dp[0][0])
