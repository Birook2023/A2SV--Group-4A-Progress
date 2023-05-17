n = int(input())
roads = [list(map(int, input().split())) for _ in range(n)]
count = 0
for i in range(n):
    for j in range(i + 1, n):
        if roads[i][j] == 1:
            count += 1
print(count)
