class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        
        n, m, i, j = len(word1), len(word2),  0, 0
        merge = ""
        while i < n and j < m:            
            if word1[i] == word2[j]:
                if word1[i:] > word2[j:]:
                    merge += word1[i]
                    i+= 1
                else:
                    
                    merge += word2[j]
                    j += 1     
            else:
                if word1[i] > word2[j]:
                    merge += word1[i]
                    i+= 1
                else:
                    merge += word2[j]
                    j += 1 
            
        if i < len(word1):
            merge += word1[i:]
        else:
            merge += word2[j:]
        return merge
        
