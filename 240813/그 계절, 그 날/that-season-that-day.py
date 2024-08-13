def yun(year : int) -> bool :
    if year % 100 == 0 and year % 400 != 0: return False
    elif year % 4 == 0: return True
    else: return False

y, m, d = map(int, input().split())
days = [31, 29 if yun(y) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if  d > days[m - 1]: print("-1")
elif 3 <= m <= 5 : print("Spring") 
elif 6 <= m <= 8 : print("Summer") 
elif 9 <= m <= 11 : print("Fall") 
else : print("Winter")