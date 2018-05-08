class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        tmp = '{0:b}'.format(n)
        for i, b in enumerate(tmp):
            if i > 0 and b == tmp[i - 1]:
                return False
        return True
