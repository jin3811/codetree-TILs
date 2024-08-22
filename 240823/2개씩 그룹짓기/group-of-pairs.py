n = int(input())
arr = sorted(map(int, input().split()))
print(max([arr[i] + arr[-(i + 1)] for i in range(n)]))