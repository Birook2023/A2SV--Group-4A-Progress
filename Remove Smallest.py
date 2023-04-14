t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    i = 0
    j = i + 1
    count = n

    if n == 1:
        print("YES")
    else:
        while i < j and j < n:
            if abs(a[i] - a[j]) <= 1:
                count -= 1
                i += 1
                j += 1
            else:
                i += 1
                j += 1
        
        if count > 1:
            print ("NO")
        else:
            print("YES")
    t -= 1
