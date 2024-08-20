def sol(n):
    return 1 if n <= 1 else n * sol(n - 1)
print(sol(int(input())))