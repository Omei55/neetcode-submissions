class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mySet1 = {}
        mySet2 = {}

        for char in s:
            mySet1[char] =mySet1.get(char, 0) + 1
        for char in t:
            mySet2[char] = mySet2.get(char, 0) + 1


        return mySet1 == mySet2

        