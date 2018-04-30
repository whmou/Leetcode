class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        m_list = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--.."]
        trans_map = {}
        for w in words:
            tmp = ''
            for ch in w:
                tmp += m_list[ord(ch) - 97]
            if tmp not in trans_map:
                trans_map[tmp] = 1
        return len(trans_map)
