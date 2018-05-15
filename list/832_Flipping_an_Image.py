class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for id1, l in enumerate(A):
            l = l[::-1]
            # print l
            for id, n in enumerate(l):
                if n == 0:
                    l[id] = 1
                else:
                    l[id] = 0
            # print l
            A[id1] = l
        return A
