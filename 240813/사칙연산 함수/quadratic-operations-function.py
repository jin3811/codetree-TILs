sik = input()
a, op, b = sik.split()
a = int(a)
b = int(b)
res = 0

sik += " = "

if op == "+":
    sik = f"{sik}{a + b}"
elif op == "-":
    sik = f"{sik}{a - b}"
elif op == "*":
    sik = f"{sik}{a * b}"
elif op == "/":
    sik = f"{sik}{a // b}"
else:
    sik = str(False)

print(sik)