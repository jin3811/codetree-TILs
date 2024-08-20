n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

for i in range(1, n + 1): arr[i] += arr[i - 1]

for _ in range(m):
    q1, q2 = map(int, input().split())
    print(arr[q2] - arr[q1 - 1])