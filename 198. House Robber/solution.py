class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [0, 0] + nums
        maximum = [0, 0]  # previous maximum & current maximum
        for i in range(2, len(nums)):
            temp = max(maximum[i-1], nums[i] + maximum[i-2])
            maximum.append(temp)
        return maximum[-1]
