n, t = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
temp = 0

for i in arr:
    if i <= t:
        answer = max(temp, answer)
        temp = 0
    else:
        temp += 1

print(answer)