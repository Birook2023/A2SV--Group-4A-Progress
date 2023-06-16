class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        ordr = []
        heap = []
        curr = 0
        i = 0
        
        while i < n or heap:
            
            if not heap:
                curr = tasks[i][0]
                
            while i < n and tasks[i][0] <= curr:
                heapq.heappush(heap, [tasks[i][1], tasks[i][0], i])
                i += 1
                
            if heap:
                proces, enq, index = heapq.heappop(heap)
                ordr.append(index)
                curr += proces
                
        return ordr
