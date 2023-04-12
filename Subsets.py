class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sub_sets = []
        tempo = []

        def backtrack(index = 0):
            if index >= len(nums):
                sub_sets.append(tempo.copy())
                return sub_sets
                
            tempo.append(nums[index])
            backtrack(index+1)

            tempo.pop()
            backtrack(index+1)
        
        backtrack()

        return sub_sets
