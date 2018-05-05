class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        if S is None or len(S) == 0:
            return [0, 0]

        w_dict = {}
        for i, w in enumerate(widths):
            w_dict[i] = w

        total_lines = 1
        tmp_width = 0
        for s in S:
            next_w = w_dict[ord(s) - 97]
            if tmp_width + next_w <= 100:
                tmp_width += next_w
            else:
                total_lines += 1
                tmp_width = next_w

        return [total_lines, tmp_width]
