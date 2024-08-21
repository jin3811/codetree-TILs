n=int(input())

print(*sorted([input() for i in range(n)]), sep='\n')