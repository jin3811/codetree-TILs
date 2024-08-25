n = int(input())
color = 0
board = [[color for i in range(201)] for i in range(201)]

for _ in range(n):
    x1, y1, x2, y2 = map(lambda x : int(x) + 100, input().split())

    for y in range(y1, y2):
        for x in range(x1, x2):
            board[y][x] = color
    
    color ^= 1

print(sum(map(lambda x : x.count(1), board)))