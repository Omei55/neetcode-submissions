# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def solve(root):
            if root == None:
                return 0
            lH = solve(root.left)
            if lH == -1:
                return -1
            rH = solve(root.right)
            if rH == -1:
                return -1
            
            if abs(lH - rH ) > 1:
                return -1
            
            return 1 + max(lH, rH)
        x = solve(root)
        if x == -1:
            return False
        return True
        
        
    
  

        