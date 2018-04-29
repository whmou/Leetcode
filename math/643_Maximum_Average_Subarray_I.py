class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if nums is None or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        tmp_max = sum(nums[:k])
        tmp_val = tmp_max
        start_idx = 0
        end_idx = k
        while end_idx < len(nums):
            tmp_val = tmp_val + nums[end_idx] - nums[start_idx]
            tmp_max = max(tmp_val, tmp_max)
            end_idx += 1
            start_idx += 1
        return float(tmp_max) / k
