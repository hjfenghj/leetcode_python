class Solution:
    def generateParenthesis(self, n):
        res = set()
        if n == 1:
            res = {"()"}
            return list(res)
        else:
            for A in self.generateParenthesis(n-1):
                for i in range(len(A)+2):
                    res.add(A[0:i]+'()'+A[i:])

            return list(res)

A = Solution()
B = A.generateParenthesis(3)
print(B)
