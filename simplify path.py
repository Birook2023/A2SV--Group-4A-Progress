class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []
        D = path.split('/')

        for d in D:
            if d == '' or d == '.':
                continue
            elif d == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(d)
        
        return '/' + '/'.join(stack)
