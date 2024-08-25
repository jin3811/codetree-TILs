n, _ = map(int, input().split())
querys = input()
board = [list(map(int, input().split())) for i in range(n)]
dx = [0, 1, 0, -1] # 북 동 남 서
dy = [-1, 0, 1, 0]
d = 0

curX ,curY = n // 2, n // 2
answer = board[curY][curX]

for query in querys:
    if query == "R":
        d = (d + 1) % 4

    elif query == "L":
        d = (d + 3) % 4

    else :
        newX = curX + dx[d]
        newY = curY + dy[d]
        if newX < 0 or newX >= n or newY < 0 or newY >= n :
            continue
        
        curX, curY = newX, newY
        answer += board[curY][curX]

print(answer)