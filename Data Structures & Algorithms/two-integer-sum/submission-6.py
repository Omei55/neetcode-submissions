class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        n = len(nums)
        
        for i in range(0,n):
            remaining = target - nums[i]
            if remaining in seen:
                return [seen[remaining], i]

            seen[nums[i]] = i





        