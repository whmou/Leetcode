class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """

        result_list = []
        for id, num in enumerate(findNums):
            tmp = -1
            try:
                for i in range(nums.index(num), len(nums)):
                    if nums[i] > num:
                        tmp = nums[i]
                        break
            except BaseException:
                pass
            result_list.append(tmp)
        return result_list
