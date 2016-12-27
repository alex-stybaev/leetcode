class Solution(object):
    def find_disappeared_numbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = range(1, len(nums) + 1)
        for i in range(0, len(nums)):
            result[nums[i] - 1] = 0

        return filter(lambda a: a != 0, result)


s = Solution()
print(s.find_disappeared_numbers([1,2,2,2]))