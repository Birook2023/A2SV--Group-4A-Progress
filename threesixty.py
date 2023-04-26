def found(rot):
    def find(ind, currsum):
        if ind == len(rot):
            return currsum%360 == 0
            
        return find(ind + 1, currsum - rot[ind]) or find(ind + 1, currsum + rot[ind])
        
    return find(0, 0)


r = int(input())
rotations = []

for _ in range(r):
    rotations.append(int(input()))
    
if found(rotations):
    print("YES")
else:
    print("NO")
    
    
    
