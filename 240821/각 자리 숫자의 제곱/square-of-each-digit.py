def sol(n) :
    if not n : return 0
    f = n % 10
    return f * f + sol(n // 10)

print(sol(int(input())))