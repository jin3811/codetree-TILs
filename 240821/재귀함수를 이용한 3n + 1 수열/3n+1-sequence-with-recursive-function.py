def sol(n):
    if n == 1: return 0
    if n % 2 == 1: n = 3 * n + 1
    else: n //= 2
    return 1 + sol(n)
print(sol(int(input())))