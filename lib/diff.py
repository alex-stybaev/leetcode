class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        list_s = list(s)
        list_t = list(t)

        list_s.sort()
        list_t.sort()

        for i in range(0, len(list_s)) :
            if list_s[i] != list_t[i]:
                return list_t[i]

        return list_t[-1]


s = Solution()
print(s.findTheDifference("asdesd", "easdsdf"))