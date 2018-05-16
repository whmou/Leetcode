class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        rtn = ''
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for w_id, w in enumerate(S.split()):
            if w[0] in vowel:
                rtn = '{0} {1}ma{2}'.format(rtn, w, 'a' * (w_id + 1))
            else:
                rtn = '{0} {1}ma{2}'.format(
                    rtn, w[1:] + w[0], 'a' * (w_id + 1))
        return rtn.strip()
