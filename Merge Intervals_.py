class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans=[]
        a=intervals[0]
        for i in intervals[1:]:
            if i[0]<=a[1] and i[1]>a[1]:
                a[1]=i[1]
            elif i[0]>a[1]:
                ans.append(a)
                a=i
        ans.append(a)
        return ans
