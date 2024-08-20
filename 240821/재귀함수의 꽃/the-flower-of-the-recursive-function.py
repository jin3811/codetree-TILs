def sol(cur):
    if cur <= 0 : return
    print(cur, end=" ")
    sol(cur - 1)
    print(cur, end=" ")

sol(int(input()))