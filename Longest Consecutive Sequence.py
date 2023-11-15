class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        leng = 0
        for num in nums:
            if num - 1 in sett:
                continue
            curr = 1
            while (num + curr) in sett:
                curr += 1
            leng = max(curr, leng)
        return leng
