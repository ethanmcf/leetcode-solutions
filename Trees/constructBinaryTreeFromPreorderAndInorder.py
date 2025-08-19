# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        ind_map = {}
        for i in range(len(inorder)):
            ind_map[inorder[i]] = i

        self.index = 0
        def build(start, end):
            if start > end or self.index == len(preorder):
                return

            root_val = preorder[self.index]
            root = TreeNode(root_val)
            self.index += 1

            split = ind_map[root_val]
            root.left = build(start, split - 1)
            root.right = build(split + 1, end)
            return root            
        
        return build(0, len(preorder))
