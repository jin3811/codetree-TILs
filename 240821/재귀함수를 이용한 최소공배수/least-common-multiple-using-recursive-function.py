def sol(a, b):
    return a if b == 0 else sol(b, a%b)

n = int(input())
arr = list(map(int, input().split()))

while len(arr) > 1:
    a, b = arr.pop(), arr.pop()
    arr.append(a * b // sol(a, b))
print(arr[0])