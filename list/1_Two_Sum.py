class Solution(object):
    def __init__(self):
        self.index_dict = {}
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums == None:
            return -1, -1
        for idx, num in enumerate(nums):
            if num not in self.index_dict:
                self.index_dict[target - num] = idx
            else:
                return self.index_dict[num], idx
        return -1, -1
