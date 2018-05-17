class Solution(object):
    def __init__(self):
        self.record = {}

    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if (s1, s2) in self.record:
            return self.record[(s1, s2)]
        if s1 == s2:
            self.record[(s1, s2)] = True
            return True
        if len(s1) != len(s2) or sorted(s1) != sorted(s2):
            self.record[(s1, s2)] = False
            return False
        for i in xrange(1, len(s1)):
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) or \
                    (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])):
                return True
        self.record[(s1, s2)] = False
        return False
