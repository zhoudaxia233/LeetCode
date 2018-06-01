# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        stack_curr, depth = [root], 1
        while stack_curr:
            stack_next = []
            while stack_curr:
                top = stack_curr.pop()
                if top.left:
                    stack_next.append(top.left)
                if top.right:
                    stack_next.append(top.right)
                if top.left is None and top.right is None:
                    return depth
            stack_curr = stack_next
            depth += 1
