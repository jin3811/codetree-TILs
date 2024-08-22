n,m,pre=input().split()
n,m = int(n), int(m)
arr=[]
for _ in range(n):
    a = input()
    if a.find(pre) != 0 : continue
    arr.append(a)

arr.sort()
print(arr[m-1])