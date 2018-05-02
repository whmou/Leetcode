class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        z = x ^ y
        total = 0
        while z > 0:
            if z % 2 == 1:
                total += 1
            z = z >> 1
        return total
