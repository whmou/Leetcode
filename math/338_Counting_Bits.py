class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        rtn = []
        for i in range(0, num + 1):
            rtn.append('{0:b}'.format(i).count('1'))
        return rtn
