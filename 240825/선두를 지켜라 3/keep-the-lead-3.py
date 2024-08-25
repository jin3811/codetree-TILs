n,m = map(int, input().split())
recordA = [list(map(int, input().split())) for _ in range(n)]
recordB = [list(map(int, input().split())) for _ in range(m)]

for a in range(1, n):
    recordA[a][1] += recordA[a - 1][1]
for b in range(1, m):
    recordB[b][1] += recordB[b - 1][1]

posA, posB = 0, 0
distA, distB = 0, 0
first, cur = "", ""
answer = 0

for time in range(1, recordA[n - 1][1] + 1):
    if time > recordA[posA][1] :
        posA += 1
    if time > recordB[posB][1] :
        posB += 1

    distA += recordA[posA][0]
    distB += recordB[posB][0]

    if distA > distB : cur = "A"
    elif distA < distB : cur = "B"
    else : cur = "AB"

    if first != cur:
        first = cur 
        answer += 1

print(answer)