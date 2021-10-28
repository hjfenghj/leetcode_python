class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res =[]
        ans = []
        def backtracking(n,k,index):
            if len(res) == k:
                ans.append(res[:])
                return 
            
            for i in range(index,n+1):
                res.append(i)
                backtracking(n,k,i+1)
                res.pop()
                
            
        backtracking(n,k,1)
        return ans
