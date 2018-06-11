# 解题思路：
>[题目链接](https://leetcode.com/problems/maximum-subarray/description/)

这道题很有名，并且有一个公认的最优解法，时间复杂度为O(n)，空间复杂度为O(1)，这个解法的名字叫[Kadane's Algorithm](https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane's_algorithm)。

下面举一个例子来具体说明：  
`A = [-2,1,-3,4,-1,2]`  
假设我们现在正在访问第i个元素`A[i]`(为了方便陈述，这里`i`从0开始计算)，我们假设`i=1`，则`A[i]`的值1。  

**目标**：找到以`A[i]`为结尾的序列中，包含`A[i]`的最大子序列。  

具体说，就是，找到以1结尾的序列中，包含1的最大子序列。  
以1为结尾的序列，当然就是`[-2,1]`。  
接下来我们要找到包含1的最大子序列。  

现在假设我们已经求出了这个问题的**子问题**的答案。也就是说，我们求出了 “找到以`A[i-1]`为结尾的序列中，包含`A[i-1]`的最大子序列。” 的答案。我们将这个子问题的答案记为`max_end_with(i-1)`，那么依照`Kadane's Algorithm`便有：

`max_end_with(i) = max(A[i], max_end_with(i-1) + A[i])`

也就是说，包含了`A[i]`，并且以`A[i]`为结尾的序列，其子序列的最大值包含了两种情况：  
1. 当`max_end_with(i-1)`为正数时，我们把它加上`A[i]`作为`max_end_with(i)`的结果返回；
2. 当`max_end_with(i-1)`为负数时，我们就不要`max_end_with(i-1)`这一项了，不然`A[i]`加了负数会更小，所以在这种情况下我们只返回`A[i]`。

然后，我们将当前的`max_end_with(i)`值与之前遍历得到的值中最大的一个进行比较，然后保留较大的那一个。
>假设此处的`i=3`，那么我们进行比较的双方就是：  
`max_end_with(3)` 与 max(`max_end_with(0)`,`max_end_with(1)`,`max_end_with(2)`)  

>在实际的代码中，我们并不需要存储每一个`max_end_with(i)`的值。我们只需要保存一个最大值即可。上面那样写只是为了便于阐述算法。

这样，当遍历结束之后，我们得到的`max_end_with(i)`，就是整个数组的最大子序列和。


---
