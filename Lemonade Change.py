class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        '''
         5 = 0
        10 = 1
        

[5,5,5,5,20,20,5,5,5,5]
        '''
        fives = 0
        tens = 0
        
        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                if fives < 1:
                    return False
                fives -= 1
                tens += 1
            elif bill == 20:
                if tens >= 1 and fives >= 1:
                    tens -= 1
                    fives -= 1
                elif fives >= 3:
                    fives -= 3
                else:
                    return False
        
        return True
                    
