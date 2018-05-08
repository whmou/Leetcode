class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        p_l = {2:1, 3:1,5:1,7:1,11:1,13:1,17:1,19:1}
        tmp =0
        for i in range(L, R+1):
            if '{0:b}'.format(i).count('1') in p_l:
                tmp+=1
        return tmp
