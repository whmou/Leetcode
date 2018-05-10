class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        tmp_dict = {}
        tmp_dict['q'] = 0
        tmp_dict['w'] = 0
        tmp_dict['e'] = 0
        tmp_dict['r'] = 0
        tmp_dict['t'] = 0
        tmp_dict['y'] = 0
        tmp_dict['u'] = 0
        tmp_dict['i'] = 0
        tmp_dict['o'] = 0
        tmp_dict['p'] = 0
        tmp_dict['Q'] = 0
        tmp_dict['W'] = 0
        tmp_dict['E'] = 0
        tmp_dict['R'] = 0
        tmp_dict['T'] = 0
        tmp_dict['Y'] = 0
        tmp_dict['U'] = 0
        tmp_dict['I'] = 0
        tmp_dict['O'] = 0
        tmp_dict['P'] = 0

        tmp_dict['a'] = 1
        tmp_dict['s'] = 1
        tmp_dict['d'] = 1
        tmp_dict['f'] = 1
        tmp_dict['g'] = 1
        tmp_dict['h'] = 1
        tmp_dict['j'] = 1
        tmp_dict['k'] = 1
        tmp_dict['l'] = 1
        tmp_dict['A'] = 1
        tmp_dict['S'] = 1
        tmp_dict['D'] = 1
        tmp_dict['F'] = 1
        tmp_dict['G'] = 1
        tmp_dict['H'] = 1
        tmp_dict['J'] = 1
        tmp_dict['K'] = 1
        tmp_dict['L'] = 1

        tmp_dict['z'] = 2
        tmp_dict['x'] = 2
        tmp_dict['c'] = 2
        tmp_dict['v'] = 2
        tmp_dict['b'] = 2
        tmp_dict['n'] = 2
        tmp_dict['m'] = 2
        tmp_dict['Z'] = 2
        tmp_dict['X'] = 2
        tmp_dict['C'] = 2
        tmp_dict['V'] = 2
        tmp_dict['B'] = 2
        tmp_dict['N'] = 2
        tmp_dict['M'] = 2

        result = []
        for word in words:
            same_line = True
            tmp_line = tmp_dict[word[0]]
            for id, c in enumerate(word):
                if id > 0 and tmp_line != tmp_dict[c]:
                    same_line = False
                    break

            if same_line:
                result.append(word)
        return result
