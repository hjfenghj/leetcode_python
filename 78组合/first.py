class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans =[]
        ans.append([])
        
        n = len(nums)
        for i in range(n):
            ans.append([nums[i]])
            
        if n >= 2:
            
            for k in range(2,len(nums)+1):
            
                res = []
                def backtracking(nums,k,index):
                    if len(res) == k:
                        ans.append(res[:])
                        if k == n:
                            return ans
                        else:
                            return
                    for i in range(index,len(nums)):
                        res.append(nums[i])
                        backtracking(nums,k,i+1)
                        res.pop()
                    
                backtracking(nums,k,0)
                
            return ans
        else:
            return ans
