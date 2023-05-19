n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
lis = [[] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if mat[i][j] == 1:
            lis[i].append(j+1)

for i in range(n):
    print(len(lis[i]), *lis[i])
