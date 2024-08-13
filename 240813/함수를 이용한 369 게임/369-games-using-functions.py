n,m = map(int, input().split())
print(len([i for i in range(n, m + 1) if "3" in str(i) or "6" in str(i) or "9" in str(i) or i % 3 == 0]))