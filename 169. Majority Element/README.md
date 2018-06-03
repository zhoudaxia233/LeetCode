# 解题思路：
>[题目链接](https://leetcode.com/problems/majority-element/description/)

由于我们要找的元素在数组中占一半以上，所以我们可以给数组排序，然后取数组中间位置的元素看一下是什么，这个元素就是我们要找的。具体地，我们要取中间的哪个位置呢？这里分两种情况来讨论：  
1. 数组长度为奇数
2. 数组长度为偶数  

如下图：  

![](https://raw.githubusercontent.com/zhoudaxia233/LeetCode/master/169.%20Majority%20Element/169.png)

---
关于Python的解法：  
第0种解法就是按照以上思路写的，而第1种解法比较有趣。由于我们要找的元素占数组一半以上，所以我们有很大概率直接找到这个元素，因此我们利用随机性来解。
