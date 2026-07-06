class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mySet = {}
        for i in nums:
            if i in mySet:
                return True
            mySet[i] = 1

        return False
        