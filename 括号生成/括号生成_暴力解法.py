class Solution(object):

    def generateParenthesis(self, n):

        def gener(s):
            if len(s) == 2*n:
                if vaild(s):        
                    ans.append("".join(s))
            else:
                # if vaild(s):
                    s.append('(')
                    gener(s)
                    s.pop()
                    s.append(')')
                    gener(s)
                    s.pop()
                
                
                
        def vaild(S):
            left = right = 0
            for letter in S:
                
                if letter == '(':  left+=1
                else:              right+=1
                if left < right:
                    return False
            return left == right
        
        ans = []
        gener([])
        
        return ans
    
