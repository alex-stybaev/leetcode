import math
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        m = 1
        for count in range (1,n):
            m = n ^ count

        return m

s = Solution()
print(s.bulbSwitch(8))