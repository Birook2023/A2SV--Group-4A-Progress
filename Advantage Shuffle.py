class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sorted_nums1 = sorted(nums1)[::-1]
        sorted_nums2= sorted([num, i] for i, num in enumerate(nums2))[::-1]
        ans = [-1 for x in range(len(nums1))]
        s, e = 0, len(nums1) -1
        
        for num, i in sorted_nums2:
            if sorted_nums1[s] > num:
                ans[i] = sorted_nums1[s]
                s += 1
            else:
                ans[i] =sorted_nums1[e]
                e -= 1
        
        return ans
