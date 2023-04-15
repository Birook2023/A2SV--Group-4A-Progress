class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        f = Counter(arr)
        n = len(arr)
        ans = 0
        tar = n//2
        for i in sorted(f, key=f.get, reverse=True):
            tar -= f[i]
            ans += 1
            if tar <= 0:
                break
        return ans
