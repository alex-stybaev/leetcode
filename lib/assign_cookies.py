class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: int
        :rtype: int
        """
        count = 0
        i = 0
        j = 0
        g.sort(reverse=True)
        s.sort(reverse=True)
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                count += 1
                i += 1
                j += 1
            else:
                i += 1
        return count

s = Solution()

print(s.findContentChildren([1,2], [1,2,3]))

