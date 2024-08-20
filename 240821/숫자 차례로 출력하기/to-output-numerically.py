def sol1(cur, n):
    if cur > n : return
    print(cur, end=" ")
    sol1(cur + 1, n)

def sol2(cur, n):
    if cur > n : return
    sol2(cur + 1, n)
    print(cur, end=" ")

n = int(input())
sol1(1, n)
print()
sol2(1, n)