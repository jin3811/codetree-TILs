n = int(input())
l = range(1,10)
for i in range(n):
    for j in range(n):
        print(l[(i * n + j) % 9], end=" ")
    print()