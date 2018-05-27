# 解题思路：
>[题目链接](https://leetcode.com/problems/flipping-an-image/description/)

这题太简单了，不需要思路。我想了想，好像没有时间复杂度低于O(n<sup>2</sup>)的解法。

---
关于Python的解法：`^`是异或操作(位运算)。用1与一个二进制的位异或，可以把1变成0，把0变成1。  
由于此题强调了矩阵和矩阵内的行都非空，所以我们不用在代码里判断其是否为`None`。如果题目没有说明的话，我们必须进行判断，否则，for循环那里将会抛出 ***'NoneType' object is not iterable*** 的异常。