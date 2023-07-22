class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        new = []
        n = len(gas)
        
        for i in range(n):
            new.append(gas[i] - cost[i])
        ch = 0
        ind = -1

        if sum(new) >= 0:
            for i in range(n):
                ch+=(new[i])
                if ch < 0:
                    ind = -1
                    ch = 0
                elif ind == -1:
                    ind = i
            return ind
        return -1
