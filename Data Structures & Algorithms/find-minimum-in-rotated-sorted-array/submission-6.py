class Solution:
    def findMin(self, nums: List[int]) -> int:
        l ,  r = 0 , len(nums) - 1
        mini = float("inf")

        while l <= r:
            mid = (l  + r) // 2
            if nums[mid]< nums[r]:
                mini = min(nums[mid], mini)
                r = mid - 1
            else:
                mini = min(nums[l], mini )
                l = mid + 1
            
        return mini



        