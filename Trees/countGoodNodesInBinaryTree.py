# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return 1 + self.helper(root.left, root.val) + self.helper(root.right, root.val)

    def helper(self, root, maxVal):
        if not root:
            return 0
        add = 0
        if root.val >= maxVal:
            add = 1
        maxVal = max(maxVal, root.val)
        return add + self.helper(root.left, maxVal) + self.helper(root.right, maxVal)
