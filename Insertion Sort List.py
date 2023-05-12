arr, cur = [], head
        
        while cur:
            arr.append(cur.val)
            cur = cur.next
        arr.sort()
        
        cur, i = head, 0
        
        while cur:
            cur.val = arr[i]
            i+= 1
            cur = cur.next
        
        return head
