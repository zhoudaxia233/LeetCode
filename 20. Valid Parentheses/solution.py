class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        match = {'(': ')', '{': '}', '[': ']'}
        stack = []  # list of left side of parentheses
        for i in s:
            if i in match.keys():
                stack.append(i)
            else:
                if len(stack) == 0 or i != match[stack.pop()]:
                    return False
        return len(stack) == 0
