class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1 = 0
        n2 = 0
        for c in num1:
            n1 *= 10
            n1 += ord(c) - 48
        for c in num2:
            n2 *= 10
            n2 += ord(c) - 48
        return str(n1 * n2)
