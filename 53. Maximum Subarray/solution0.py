class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far = max_end_here = nums[0]
        for num in nums[1:]:
            max_end_here = max(num, max_end_here + num)
            max_so_far = max(max_so_far, max_end_here)
        return max_so_far
