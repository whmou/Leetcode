class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = x
        while right >= left:
            mid = (left + right) / 2
            reuslt = mid ** 2
            if reuslt == x:
                return mid
            elif reuslt < x:
                left = mid + 1
            else:
                right = mid - 1
        return right
