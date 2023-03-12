class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        arr = [(position[i],speed[i]) for i in range(len(position))]
        arr.sort(reverse=True)
        
        stack = []
        fleet = 0
        
        for p, s in arr:
            curr = (target-p)/s
            if len(stack)==0 or curr > stack[-1]:
                stack.append(curr)
                fleet+=1
           
        return fleet
        
