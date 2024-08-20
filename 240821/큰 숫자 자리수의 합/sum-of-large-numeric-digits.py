def sol(n) :
    if n == 0 : return 0
    return n % 10 + sol(n // 10)

a,b,c=map(int,input().split())
print(sol(a*b*c))