class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a = len(s1)
        S1 = {}
        S2 = {}

        for i in s1:
            S1[i] = S1.get(i,0) + 1
        start = 0
        for right in range(len(s2)):
            S2[s2[right]] = 1 + S2.get(s2[right],0)
            if right - start + 1 > len(s1):
                S2[s2[start]] -= 1
                if S2[s2[start]] == 0:
                    del S2[s2[start]]
                start += 1

            if S2 == S1:
                return True
        
        return False





        