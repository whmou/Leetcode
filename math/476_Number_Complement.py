class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        bit_len = len("{0:b}".format(num))
        a = 2 ** bit_len - 1
        return a - num
