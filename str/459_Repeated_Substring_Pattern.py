class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None:
            return False
        ch_len = 1
        max_len = len(s) / 2 + 1
        chk_idx_start = ch_len
        chk_idx_end = chk_idx_start + ch_len
        while ch_len <= max_len:
            if s[:ch_len] == s[chk_idx_start: chk_idx_end]:
                if chk_idx_end >= len(s):
                    return True
                chk_idx_start = chk_idx_end
                chk_idx_end = chk_idx_end + ch_len
            else:
                ch_len += 1
                chk_idx_start = ch_len
                chk_idx_end = chk_idx_start + ch_len
                continue
        return False
