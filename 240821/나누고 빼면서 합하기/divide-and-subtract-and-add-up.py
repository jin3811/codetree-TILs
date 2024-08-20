n, m = map(int, input().split())
arr = list(map(int, input().split()))
res = 0
while m >= 1:
    res += arr[m - 1]
    if m % 2 == 1 : m -= 1
    else: m //= 2
print(res)