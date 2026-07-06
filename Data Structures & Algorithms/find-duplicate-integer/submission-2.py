class Solution:
    def findDuplicate(self, nums):
        for num in nums:
            index = abs(num)
            
            if nums[index] < 0:
                return index
            
            nums[index] = -nums[index]