class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = []
        res = Counter(words[-1])
        
        for word in words:
            res &= Counter(word)
            
        for i in res:
            ans += [i] * res[i]
        
        return ans
