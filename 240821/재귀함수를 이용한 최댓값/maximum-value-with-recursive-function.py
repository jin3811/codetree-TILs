def sol(idx) :
    global n, arr
    if idx == n - 1 : return arr[idx]
    a = sol(idx + 1)
    return arr[idx] if arr[idx] > a else a

n = int(input())
arr = list(map(int, input().split()))
print(sol(0))