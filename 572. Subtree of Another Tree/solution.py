class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s is None:
            return False
        if self.isSametree(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
    def isSametree(self, a, b):
        if a and b:
            return a.val == b.val and self.isSametree(a.left, b.left) and self.isSametree(a.right, b.right)
        return a is b
