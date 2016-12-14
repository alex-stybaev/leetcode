class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)
        left = 0
        right = len(nums) - 1
        while sorted_nums[left] + sorted_nums[right] != target:
            if sorted_nums[left] + sorted_nums[right] > target:
                right -= 1
            else:
                left += 1

        return [nums.index(sorted_nums[left]), nums.index(sorted_nums[right])]

s = Solution()
print(s.twoSum([4, 2, 7, 11, 15], 9))