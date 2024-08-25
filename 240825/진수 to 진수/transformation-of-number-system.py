def sol(n : int, base : int) -> str :
    res = []
    while n : 
        res.append(n % base)
        n //= base
    
    return "".join(map(str, res))

a,b = map(int, input().split())
print(sol(int(input(), a), b))