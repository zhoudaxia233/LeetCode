class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        s = a ^ b
        carry = (a & b) << 1
        return s + carry
