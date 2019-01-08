class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        queue = []        
        for p in sorted(people, key=lambda p: (-p[0], p[1])):
            queue.insert(p[1], p)
        return queue
