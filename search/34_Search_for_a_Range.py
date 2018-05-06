class Solution(object):
    def bS_helper(self, nums, target, id_search=False):
        left = 0
        right = len(nums) - 1
        while right >= left:
            mid = (left + right) / 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1

        return left if id_search else -1

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        r = self.bS_helper(nums, target)
        if r == -1:
            return [-1, -1]
        else:
            return [self.bS_helper(nums, target - 0.5, True),
                    self.bS_helper(nums, target + 0.5, True) - 1]
