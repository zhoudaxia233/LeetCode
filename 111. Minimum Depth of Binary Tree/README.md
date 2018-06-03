# 解题思路：
>[题目链接](https://leetcode.com/problems/minimum-depth-of-binary-tree/description/)

求一棵二叉树的最浅深度，也就是求根节点到与它距离最近的叶节点这条路径上的**节点总数**。  
首先我们要知道什么是叶节点，叶节点就是既没有左子树又没有右子树的节点。  
然后，我们就可以做题了，这道题和 [104. Maximum Depth of Binary Tree](https://github.com/zhoudaxia233/LeetCode/tree/master/104.%20Maximum%20Depth%20of%20Binary%20Tree) 差不多，依然有深度优先和广度优先两种解法。但由于我们是在找最浅深度，显然**广度优先搜索**更优。

---
关于Python的解法：  
深度优先搜索我用的是递归法。我们分别得到左子树和右子树的深度，然后返回其中较小的那一个值(由于只有两个值参与比较，所以此处我用了`min`函数，其实和比较大小的函数是等价的)。这里有一点需要注意的是，我们还得判断一下，较小的这个深度值是否为0，如果为0的话，那就说明左子树不存在，进而说明叶节点在右子树的那一侧。此时，我们就不能返回较小值，而要返回较大值。
>例如，[1, null, 2] 这棵二叉树，左子树不存在，右子树只有一个叶节点，那么其“最浅深度”应该是2，而不是1。

  
广度优先搜索我用的是非递归的方式，创建了两个栈。一个栈用来存储当前层次要遍历的节点(假设叫`stack_curr`)，另一个栈用来存储下一个层次要遍历的节点(假设叫`stack_next`)。  
初始化时，我们将根节点 入`stack_curr`栈，将当前深度记为1(因为根节点存在，按照最浅深度的定义，其最浅深度至少是1)。  
然后，我们将根节点出栈，并分别访问它的左孩子和右孩子。  
如果孩子节点存在，则将其入栈(注意，此处入的是下一个层次要遍历的节点的栈，即`stack_next`)；  
如果左孩子和右孩子都不存在，那就说明，当前访问的节点是一个**叶节点**，由于我们采用的是广度优先遍历，所以第一个遇到的叶节点一定是最浅深度路径上的叶节点，所以我们立刻返回当前深度。