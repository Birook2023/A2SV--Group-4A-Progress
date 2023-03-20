class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        mini, maxi  = max(weights) , sum(weights) 
        mini_maxi = mini
        
        while mini <= maxi: 
            mid = (mini + maxi) //2
            req_days = 1
            curr_weight = 0
            
            for weight in weights: 
                if curr_weight + weight > mid: 
                    req_days += 1
                    curr_weight = 0
                curr_weight += weight 
            
            if req_days <= days: 
                mini_maxi = mid 
                maxi = mid - 1
            else: 
                mini = mid + 1
                
        return mini_maxi
