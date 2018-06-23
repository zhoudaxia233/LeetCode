# 解题思路：
>[题目链接](https://leetcode.com/problems/same-tree/description/)

利用递归方法，先判断根节点是否一样，再判断左子树和右子树。

---
关于Python的解法：  
最后的 `return p is q`，是在说，如果`p`和`q`均为`None`，则返回`True`，否则返回`False`。
