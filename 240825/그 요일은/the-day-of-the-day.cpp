days = [31,29,31,30,31,30,31,31,30,31,30,31]
dayName = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
m1,d1,m2,d2 = map(int, input().split())
target = dayName.index(input())

day = 0

if m1 == m2 : 
    day = d2 - d1
else :
    day = days[m1 - 1] - d1
    for m in range(m1 + 1, m2):
        day += days[m - 1]
    day += d2

print(day // 7 + (1 if day % 7 >= target else 0))