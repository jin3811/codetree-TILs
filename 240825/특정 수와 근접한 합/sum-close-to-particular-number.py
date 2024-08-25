n, s = map(int, input().split())
arr = list(map(int, input().split()))
total = sum(arr)
answer = 0

for i in range(0, n):
    for j in range(i + 1, n):
        temp = total - arr[i] - arr[j]
        
        if abs(s - answer) > abs(s - temp):
            answer = temp

print(abs(s - answer))