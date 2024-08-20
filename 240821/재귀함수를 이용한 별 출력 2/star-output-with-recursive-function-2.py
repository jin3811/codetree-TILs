def sol(cur):
    if cur <= 0 : return
    print("* " * cur)
    sol(cur - 1)
    print("* " * cur)

sol(int(input()))