class Solution:
    def compress(self, chars: List[str]) -> int:
        back = 0
        ind = 0
        n =len(chars)
        
        for pos , char in enumerate(chars):
            if pos==n-1 or char!=chars[pos+1]:
                chars[ind]=char 
                ind+=1 
                
                if pos>back:
                    times=pos-back+1 
                    
                    st_time=str(times)
                    for i in st_time: 
                        chars[ind]=i  
                        ind+=1 
                back=pos+1 
        return ind 
