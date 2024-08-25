n = int(input())
arr = ["g" for i in range(n * 200 + 11)]
pos = n * 100 + 5

for _ in range(n):
    x, d = input().split()
    x = int(x)

    if d == 'R':
        for i in range(pos, pos+x):
            arr[i] = "b"
        
        pos += x - 1
    
    else :
        for i in range(pos - x + 1, pos + 1):
            arr[i] = 'w'
        
        pos -= x - 1

print(arr.count('w'), arr.count('b'))