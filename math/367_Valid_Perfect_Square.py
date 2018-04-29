class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        i, j = 0, num
        while i <= j:
            mid = (i + j) / 2
            sqare_mid = mid**2
            if sqare_mid > num:
                j = mid - 1
            elif sqare_mid < num:
                i = mid + 1
            else:
                return True

        return False
