class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        currMax = max(arr)
        ans = []
        while currMax > 1:
            maxInd = arr.index(currMax)
            if maxInd + 1 == currMax:
                currMax -= 1 
                continue
            else:
                arr[0:maxInd+1]=reversed(arr[:maxInd+1])
                ans.append(maxInd+1)
            
            arr[:currMax] = reversed(arr[:currMax])
            ans.append(currMax)
            currMax -= 1
        
        return ans  
            
