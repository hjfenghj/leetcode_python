class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        DICT= {
            '[':1,']':1,'{':2,'}':2,'(':3,')':3
            }
        label_1 = ['{','(','[']
        label_2 = [']','}',')']
        if s[0] in label_2:
            print(-1)
            return False
        for label in s:
            
            if label in label_1:
                sign = 'L'
            else:
                sign = 'R'
            
            if sign == 'L':
                stack.append(label)
            else:
                if stack:
                    if DICT[label] == DICT[stack[-1]]:
                        stack.pop()
                    else:
                        print(-1)
                        return False
                else:#这时候需要进栈，需要判断栈是否没空，如果是空的就出会出现栈头为右字符的情况
                    print(-1)
                    return False
        
        if not stack:
            print(1)
            return True
        else:
            print(-1)
            return False
        
AA = Solution()
AA.isValid('()')
            
