class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        x = int(str(x)[::-1])
        result = x * sign
        return 0 if result > 2**31 - 1 or result < -2**31 else result
