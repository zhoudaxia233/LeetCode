class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import random    
        while True:
            i = random.choice(nums)
            if nums.count(i) > (len(nums)//2):
                return i
