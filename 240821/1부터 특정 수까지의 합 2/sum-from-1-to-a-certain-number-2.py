def sol(n):
    if n <= 1 : return n
    return n + sol(n - 1)

print(sol(int(input())))