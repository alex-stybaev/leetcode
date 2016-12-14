class Solution(object):
    @staticmethod
    def intersection(nums1, nums2):
        nums1.sort()
        nums2.sort(reverse=False)
        result = []
        j = 0
        i = 0
        while 1:
            if i >= len(nums1) or j >= len(nums2):
                break
            if nums1[i] == nums2[j]:
                if result.count(nums1[i]) == 0:
                    result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
        return result


print(Solution.intersection([3,7,2], [3,2,2,4]))