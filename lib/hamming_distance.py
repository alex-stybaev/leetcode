class Solution(object):
    def hamming_distance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return str(bin(x ^ y)).count("1")


s = Solution()
print(s.hamming_distance(1, 4))
