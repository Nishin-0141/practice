n = int(input())
a = list(map(int, input().split()))
b = [0]*(n+1)
for i in range(1, n+1):
    b[i - 1] = a[i] * i
ans = ''
for i in range(len(b)):
    ans += str(b[i]) + ' '
print(ans)
