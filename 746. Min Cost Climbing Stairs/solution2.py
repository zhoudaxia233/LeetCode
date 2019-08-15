class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp1 = 0
        dp2 = 0
        for i in range(2, n+1):
            dp = min(dp2 + cost[i-2], dp1 + cost[i-1])
            # dp为跳到了i级台阶花费的最小cost
            # 由于我们已经跳到了i级台阶，并且要继续跳到i+1，所以要进行变量的更新，
            # 没跳到i级台阶之前距离为1的台阶现在距离为2: {(i-1) - (i-2) == 1 => i - (i-2) == 2},
            # 没跳到i级台阶之前站的台阶现在距离为1: {(i-1) - (i-1) == 0 => i - (i-1) == 1},
            # 因此要做如下更新：
            dp2 = dp1
            dp1 = dp
        return dp1
