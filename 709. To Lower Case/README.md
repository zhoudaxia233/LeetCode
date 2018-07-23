# 解题思路：
>[题目链接](https://leetcode.com/problems/to-lower-case/description/)

这道题最简单的解法就是用Python的自带函数`lower()`。除此之外，还有另一种解法。在此之前，我们需要先了解Python的两个内置函数，`ord()`和`chr()`：
> `ord()`，接收一个Unicode的字符表示，返回一个Unicode的整型表示。  
e.g. `ord('a') -> 97`

> `chr()`，接收一个Unicode的整型表示，返回一个Unicode的字符表示。  
e.g. `chr(97) -> 'a'`

---
