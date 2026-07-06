class Solution:
    def trap(self, height: List[int]) -> int:
        leftWall = 0
        rightWall = 0
        n = len(height)
        maxRight = [0] * n
        maxLeft = [0]*n

        for i in range(n):
            j = -i-1
            maxLeft[i] = leftWall
            maxRight[j] = rightWall
            leftWall = max(leftWall, height[i])
            rightWall = max(rightWall, height[j])

        sum = 0
        for i in range(n):
            pot = min(maxRight[i],maxLeft[i])
            sum += max(0,pot - height[i])

        return sum
        