n = int(input())
print(min(sorted(filter(lambda x : x.split()[2] == "Rain", [input() for i in range(n)]))))