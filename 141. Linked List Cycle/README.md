# 解题思路：
>[题目链接](https://leetcode.com/problems/linked-list-cycle/description/)

判断链表是否有闭环，第一个想法就是创建一个集合，把访问过的节点都丢进去，如果发现当前访问的节点在集合内，就说明链表有闭环；如果发现当前节点是None，说明已经到了链表尾部，则不存在闭环。但这个想法的空间复杂度是O(n)。  
另一个想法就是快慢指针法。设置一快一慢两个指针，如果这两个指针“相遇”了，那就说明存在闭环；
>可以联想运动会的长跑比赛，第一名经常可以做到超过最后一名一圈以上，他们在跑道上肯定会相遇。

如果快指针指向了None节点，即到达了链表的尾节点，则当前链表不存在闭环。

---
关于Python的解法：  
虽然想法很简单，但我第一次实现还是出了点小错误。原因就是边界条件判断起来比较麻烦。比如：
```
if head is None or head.next is None
```
或者是
```
while fast and fast.next
```
然后我在讨论区发现了一个利用**异常处理**来规避所有边界条件判断语句的解法，如下：  
[Except-ionally fast Python Solution](https://leetcode.com/problems/linked-list-cycle/discuss/44494/Except-ionally-fast-Python)

我的解法在他的基础上做了一点小小的修改，不知道算不算画蛇添足\_(:3」∠)_