# 解题思路：
>[题目链接](https://leetcode.com/problems/diameter-of-binary-tree/description/)

这条最长路径要么经过了这棵二叉树的根节点，要么经过了这棵二叉树的某棵子树的根节点。我们可以用反证法来证明这个结论。假设这条最长路径不经过这颗子树的根节点，那么它的路径只是这颗子树的真子集，那么其长度就不是最长的，因此假设不成立。

理解了以上这段话，那这道题就很简单了。

---
关于Python的解法：  
深度优先遍历，每遍历到一个节点，分别计算其左子树深度与右子树深度，然后求和，并将其与当前已存储的最长值进行比较，如果大于最长值，则更新之。
