#右指针是定位的作用,当右指针指向的元素小于target的时候停止运动，那么左指针只要在右指针的右边就说明指向了target的第一个元素或者比target大的元素，就可以得到左指针的位置
#target+1开始寻找右指针。当target+1的时候，右指针停止的位置是原来target的最后一个数字，那么当左指针跑到右边的时候就已经是原来target最后一位位置的后一位了。left-1就是最后一位的位置

###return left
class Solution(object):
    def searchRange(self,nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def left_func(nums,target):
            n = len(nums)-1
            left = 0
            right = n
            while(left<=right):
                mid = (left+right)//2
                if nums[mid] >= target:
                    right = mid-1
                if nums[mid] < target:
                    left = mid+1
            return left
        a =  left_func(nums,target)
        b = left_func(nums,target+1)
        if  a == len(nums) or nums[a] != target:
            return [-1,-1]
        else:
            return [a,b-1]
          
          
 #return right
class Solution(object):
    def searchRange(self,nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def left_func(nums,target):
            n = len(nums)-1
            left = 0
            right = n
            while(left<=right):
                mid = (left+right)//2
                if nums[mid] >= target:
                    right = mid-1
                if nums[mid] < target:
                    left = mid+1
            return right
        a =  left_func(nums,target)
        b = left_func(nums,target+1)
        if  a+1 == len(nums) or nums[a+1] != target:
            return [-1,-1]
        else:
            return [a+1,b]
