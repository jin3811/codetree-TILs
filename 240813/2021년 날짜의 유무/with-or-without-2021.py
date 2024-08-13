m, d = map(int, input().split())
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if  m > 12 or d > days[m - 1]: print("No")
else: print("Yes")