class Solution(object):
    def min_moves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        count = 0;
        while 1:
            if not self.is_equal(nums):
                increment(nums);
                count += 1
            else:
                break;
        return count;


    def is_equal(self, nums):
        for i in range(0, len(nums)):
            if nums[i] != nums[i+1]:
                return False
        return True
