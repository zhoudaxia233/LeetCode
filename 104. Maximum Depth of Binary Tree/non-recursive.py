# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        current_level, depth = [root], 0
        while current_level:
            next_level = []
            while current_level:
                top = current_level.pop()
                if top.left:
                    next_level.append(top.left)
                if top.right:
                    next_level.append(top.right)
            current_level = next_level
            depth += 1
        return depth
