class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top , bottom = 0, rows-1
        while top <= bottom:
            midRow = (top + bottom) // 2
            if target > matrix[midRow][-1]:
                top = midRow + 1
            elif target < matrix[midRow][0]:
                bottom = midRow - 1
            else:
                break
            
        if not (top <= bottom):
            return False
        midRow = (top + bottom) // 2
        left = 0
        right = cols - 1
        while left<=right:
            mid = left + (right- left)//2
            if target > matrix[midRow][mid]:
                left = mid + 1
            elif target < matrix[midRow][mid]:
                right = mid - 1
            else:
                return True
        return False

        
        


        