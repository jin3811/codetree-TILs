def sol(n):
    return 0 if n <= 0 else n + sol(n - 2)
print(sol(int(input())))