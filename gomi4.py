n, m = map(int, input().split())
if n <= m:
    num = [0]*(m+1)
    num[n - 1] = 1
    for i in range(n, m + 1):
        cnt = 0
        for j in range(n):
            cnt += num[j + i - n]
        num[i] = cnt
    print(num[m])
else:
    num = [0]*(n + 1)
    num[n - 1] = 1
    print(num[m])
