class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if ransomNote is None or ransomNote == "":
            return True
        if magazine is None or ransomNote == "":
            return False

        rans = list(ransomNote)
        mag = list(magazine)
        if len(mag) <= len(rans):
            return False
        for i in range(0, len(rans)):
            try:
                mag.remove(rans[i])
            except ValueError:
                return False
        return True


s = Solution()

r = s.canConstruct("a", "b")
print(r)