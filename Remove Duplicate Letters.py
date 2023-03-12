class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        res = []
        c = Counter(s)
        
        for ch in s:
            c[ch] -= 1
            if ch in res:
                continue
            while res and res[-1] > ch and c[res[-1]]:
                res.pop()
            res.append(ch)
        return ''.join(res)
