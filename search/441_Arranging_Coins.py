class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        rtn = 0
        low = 1
        high = n
        check_N = (1 + n) / 2
        while(True):

            tmp = (1 + check_N) * check_N / 2
            if tmp == n:
                return check_N
            elif tmp > n:
                if tmp - check_N <= n:
                    return check_N - 1
                else:
                    high = check_N - 1
                    check_N = (low + high) / 2

            else:
                low = check_N + 1
                check_N = (low + high) / 2
