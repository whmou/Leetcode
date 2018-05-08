class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        num_str = ''.join(map(str, nums))
        num_list = num_str.split('0')
        return len(max(num_list))
