n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

sol = "No"
for i in range(len(a) - len(b) + 1):
    if a[i : i + len(b)] == b:
        sol = "Yes"

print(sol)