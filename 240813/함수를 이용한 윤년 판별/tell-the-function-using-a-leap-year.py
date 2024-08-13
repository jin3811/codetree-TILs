def sol(year : int) -> bool :
    if year % 100 == 0 and year % 400 != 0:
        return False
    elif year % 4 == 0:
        return True
    else: 
        return False

print(str(sol(int(input()))).lower())