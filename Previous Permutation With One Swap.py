class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        i = n - 1
        Max = [arr[-1], n-1]
        while i >= 0:
            if arr[i] > Max[0]:
                Max = [arr[i], i]
                print(Max)
                Max2 = arr.index(max(arr[i+1:]))
                print(Max2)
                arr[Max[1]], arr[Max2] = arr[Max2], arr[Max[1]]
                return arr

            i -= 1
        return arr
