class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        i, j = 0, n - 1
        count = 0
        
        while i <= j:
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
            count += 1
        
        return count
