t = int(input())

while t:
    a, b = list(map(int, input().split()))
    print(min(a, b, (a + b)// 4))
    t -= 1
