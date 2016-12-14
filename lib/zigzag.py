class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        list = self.sequence(len(s), numRows)
        result = [''] * numRows
        for i in range(0, len(s)):
            result[list[i]] += s[i]
        return ''.join(result)

    def sequence(self, s, numRows):
        seq = list(range(0, numRows))
        reversed_list = list(range(1, numRows - 1))
        reversed_list.reverse()
        seq[len(seq):] = reversed_list
        result = []
        while len(result) < s:
            result.extend(seq)
        return result[:s]

s = Solution()
print(s.convert("PAYPALISHIRING", 3))