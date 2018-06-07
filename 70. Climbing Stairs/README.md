# 解题思路：
>[题目链接](https://leetcode.com/problems/climbing-stairs/description/)

>以下4+1个方法是逐步优化的，从最烂的算法到最屌的算法，所以不要急，一步一步来。

假设我们要上第i层台阶。每次上台阶我们有两种策略，一种是迈一大步，上两层；一种是迈一小步，上一层。因此，第i层台阶有两种上法：第一种，从第(i-2)层迈一大步，第二种，从第(i-1)层迈一小步。于是，可得：

>`nums_of_ways_to_step[i] = nums_of_ways_to_step[i-2] + nums_of_ways_to_step[i-1]`

看起来就是一个递归问题，于是我们得到了解法1：

解法1：
```
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-2) + self.climbStairs(n-1)
```
如果仔细分析，我们会发现上面的解法1有很多问题。比如，我们进行了很多重复性的计算。例如，当我们需要计算第i层的方法数的时候，我们求的是i-2和i-1层，而当我们求第i-1层的方法数的时候，我们求的是i-3和i-2，此时我们已经计算了两次i-2了。如下图：

![](https://raw.githubusercontent.com/zhoudaxia233/LeetCode/master/70.%20Climbing%20Stairs/70.png)

因此，我们可以利用**动态规划**的思想，把中间结果存储起来，等我们需要的时候直接访问，就不会发生重复计算的问题了。解法如下：

解法2：
```
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = [None] * (n + 1)
        return self.memo(n, memo)
    
    def memo(self, n, memo):
        if memo[n] is not None:
            return memo[n]
        if n == 1:
            res = 1
        elif n == 2:
            res = 2
        else:
            res = self.memo(n-2, memo) + self.memo(n-1, memo)
        memo[n] = res
        return res

```
虽然上面的动态规划解法看起来很赞，但它是一个递归方法，需要一个栈来存储，如果存储超过一定深度的话，就会抛出一个`RecursionError`，提示我们超过了最大递归深度。为此，我们还可以进一步优化，使用一个自底向上的方法，如下：

解法3：
```
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        memo = [None] * (n + 1)
        memo[1] = 1
        memo[2] = 2
        for i in range(3, n+1):
            memo[i] = memo[i-2] + memo[i-1]
        return memo[n]

```
由于我们不再使用递归，所以现在我们也不必担心递归超过最大深度这种问题了。但我们现在回过头来想一想，上述方法的空间复杂度是O(n)，我们使用了一个列表来存储从1到n的阶梯的方法数，然而，有必要吗？  
并没有必要！  
我们之所以要存这个东西，是因为我们在使用递归过程中不断需要获取重复的值，我们为了避免重复计算，所以才将它们存起来。然而现在我们并没有在使用递归啊！既然不需要递归，为啥还要开辟空间出来存储中间结果呢？这不是浪费吗？因此，我们有了下面的解法：

解法4：
```
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        a, b = 1, 2
        for _ in range(3, n+1):
            a, b = b, a+b
        return b
```

再仔细看看，到n层台阶的方法数等于n-2层的方法数加上n-1层的方法数，后一个的值等于前两个的和，这不就是斐波那契数列吗？因此我们有了下面的解法：

解法4 Plus：
```
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a+b
        return a
```
