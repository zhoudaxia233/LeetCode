# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.diameter = 0
        
        def depth(root):
            if root is None:
                return 0
            left, right = depth(root.left), depth(root.right)
            self.diameter = max(self.diameter, left+right)
            return max(left, right) + 1
        depth(root)
        return self.diameter
