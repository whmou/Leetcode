class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        lst = []
        for num in range(left, right + 1):
            self_dividing = True
            for d in str(num):
                if int(d) == 0 or num % int(d) != 0:
                    self_dividing = False
                    continue
            if self_dividing:
                lst.append(num)
        return lst
