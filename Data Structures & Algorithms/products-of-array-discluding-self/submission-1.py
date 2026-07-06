class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        left = 1
        right = 1

        for i in range (0,n):
            result[i] = left
            left *= nums[i]

        for j in range (n-1, -1, -1):
            result[j] *= right
            right *= nums[j]

        return result



        
