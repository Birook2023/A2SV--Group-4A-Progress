 res = []
        
        for num in arr2:
            count = arr1.count(num)

            while count > 0:
                res.append(num)
                count -= 1
        sub = []
        
        for i in arr1:
            if i not in arr2:
                sub.append(i)

        res += sorted(sub)
        
        return res
