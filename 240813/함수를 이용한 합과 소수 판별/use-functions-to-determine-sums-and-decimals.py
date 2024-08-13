def isPrime(n : int) -> bool :
    if n == 1 : return False
    if n <= 3 : return True

    for i in range(2, int(n ** 0.5) + 1) :
        if n % i == 0 :
            return False
    return True

def eachSum(n : int) -> bool:
    res = 0
    while n > 0:
        res += n % 10
        n //= 10
    return res % 2 == 0

n, m = map(int, input().split())
print(len([i for i in range(n, m + 1) if isPrime(i) and eachSum(i)]))