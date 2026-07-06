class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0,0
        mySet = {}
        n = len(s)
        maxi = 0

        while right < n:
            if s[right] in mySet:
                left = max(left, mySet[s[right]]+1)
            maxi = max(maxi, right - left +1)
            mySet[s[right]] = right
            right += 1
        return maxi
            
            
         