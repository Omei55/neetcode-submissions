class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def height(node):
            if not node:
                return 0

            lH = height(node.left)
            rH = height(node.right)

            self.diameter = max(self.diameter, lH + rH)

            return 1 + max(lH, rH)

        height(root)
        return self.diameter
