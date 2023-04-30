class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        person = 0
        
        for i in range(1, n + 1):
            person = (person + k) % i
            
        return person + 1
