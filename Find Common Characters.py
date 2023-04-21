class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        fword = words[0]
        ans = []
        counts = []
        
        for word in words:
            counts.append(Counter(word))
            
        for char in fword:
            count = 0
            for i in range(len(counts)):
                if counts[i][char] == 0:
                    break
                counts[i][char] -= 1
                count += 1
                
            if count == len(words):
                ans.append(char)
                
        return ans
