n = int(input())
lis = [list(map(int, input().split()))[1:] for _ in range(n)]
mat = [[0] * n for _ in range(n)]

for i in range(n):
    for j in lis[i]:
        mat[i][j - 1] = 1

for row in mat:
    print(*row)
