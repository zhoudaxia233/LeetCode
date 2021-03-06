# 解题思路：
>[题目链接](https://leetcode.com/problems/min-cost-climbing-stairs/)

这种求最小代价的，属于动态规划的几个常见类型题目之一。  
而解决动态规划，有三个基本步骤：
1. 构建状态函数，写出递推公式
2. 初始化(你先要给状态函数的前几项赋值，否则递推公式没办法使用)并且检查边界条件
3. 自底向上开始计算

其中，构建状态函数是重中之重。  
在这道题中，最后要求的是**登上某级台阶所需要的最小cost**，因此我们设状态函数为`f(x)`，表示到达x级台阶需要的最小cost。
> 注意，这里的`f(x)`并不包含从x台阶开始起跳的cost，而仅仅是跳到x台阶所需要的最小cost。

如何构建递推公式呢？可以遵循一个“最后一步”的技巧。我们想象一下，想跳到最后一级台阶，“最后一步”是什么呢？  
假设我们要跳`N`级台阶，由于题目中明确说了，每次可以跳一步，也可以跳两步。那么“最后一步”要么是从`N-1`级台阶跳一步，要么是从`N-2`
级台阶跳两步。而由于我们求的是最小的cost，所以取两者之间的较小值即可。

因此递推公式如下：  
`f(x) = min(f(x-1) + cost(x-1), f(x-2) + cost(x-2))`

现在有了递推公式，我们可以进入第二步骤，初始化。题目中说，“you can either start from the step with index 0, or the step with
 index 1”，也就是说，`f(0)`和`f(1)`的值均为零。
 > `f(0)`和`f(1)`分别表示从某处跳到0级台阶和跳到1级台阶所需的cost，但由于0级台阶和1级台阶都可以是起始点，所以我们从某处到起始点的这一段并没有付出任何cost，因此是零。
 
 > cost是从我们在起始点向外面跳的时候才开始计算的。这一点不要搞混了。

初始化然后检查边界条件，然后第三步骤就很简单了。所谓的自底向上开始计算，就是一个for循环，下标从小到大即可。

还有一点我们可以注意，通过观察递推公式我们发现，到达x级台阶所需要的cost仅仅和x-1级与x-2级有关。因此我们不需要一直维护一个很大的
数组，我们只需要维护两个x-1和x-2这两个状态即可。因此，我们的空间复杂度最优可以为O(1)。

---
关于Python的解法：  
其中，`solution1.py`是没有优化的常规解法，`solution2.py`是优化了空间复杂度的解法。
