def sol(n):
    if n == 1: return 1
    if n == 2: return 2
    return sol(n - 1) + sol(n // 3)
print(sol(int(input())))