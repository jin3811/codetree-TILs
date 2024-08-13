def onjeon(n : int) -> bool:
    if n % 2 == 0 : return False
    if n % 10 == 5 : return False
    if n % 3 == 0 and n % 9 != 0 : return False
    return True

n, m = map(int, input().split())
print(len([i for i in range(n, m + 1) if onjeon(i)]))