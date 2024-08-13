n=input()
print("Yes" if int(n) % 2 == 0 and (int(n[0])+int(n[1])) % 5 == 0 else "No")