# 解题思路：
>[题目链接](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/)

求一棵二叉树的深度，我们可以用深度优先搜索和广度优先搜索两种方式。

---
关于Python的解法：  
其中，深度优先搜索我用的是递归法写的，没什么可说的。  
广度优先搜索我用的是非递归的方式，创建了两个栈。一个栈用来存储当前层次要遍历的节点(假设叫`stack_curr`)，另一个栈用来存储下一个层次要遍历的节点(假设叫`stack_next`)。  
初始化时，我们将根节点 入`stack_curr`栈，将当前深度记为0。  
然后，我们将根节点出栈，并分别访问它的左孩子和右孩子。如果孩子节点存在，则将其入栈。注意，此处入的是下一个层次要遍历的节点的栈，即`stack_next`。  
若存储当前层次节点的栈`stack_curr`中没有任何节点，则说明该层次遍历完毕，此时，我们将当前深度`+1`，然后把下一个层次的节点赋给当前层次，然后初始化下一个层次的节点栈，然后继续以上操作。

关于C++的解法：  
没啥特别的，所以没啥可说的。