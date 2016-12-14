class Solution(object):

    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        unique_chars = list()
        deleted = set()
        for char in s:
            if char not in unique_chars and char not in deleted:
                unique_chars.append(char)
            elif char in unique_chars and char not in deleted:
                unique_chars.remove(char)
                deleted.add(char)
            elif char not in unique_chars and char in deleted:
                continue

        if len(unique_chars) == 0:
            return -1
        else:
            return s.index(unique_chars[0])


s = Solution()
print(s.firstUniqChar("aadadaad"))
