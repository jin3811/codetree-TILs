def sol(cur, n):
    if cur > n : return
    print("*" * cur)
    sol(cur + 1, n)

sol(1, int(input()))