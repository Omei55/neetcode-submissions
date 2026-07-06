class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        longest = 0
        mySet = set(nums)

        if n == 0:
            return 0

        for num in mySet:
            if num - 1 not in mySet:
                count = 1
                x = num
                while x + 1 in mySet:
                    x += 1
                    count += 1

                longest = max(longest, count)

        return longest
