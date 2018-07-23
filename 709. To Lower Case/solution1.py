class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        l, r = ord('A'), ord('Z')
        diff = ord('a') - ord('A')
        res = ""
        for i in str:
            num_i = ord(i)
            if l <= num_i <= r:
                res += chr(num_i + diff)
            else:
                res += i
        return res
