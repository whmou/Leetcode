class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        ids = [idx for idx, c in enumerate(S) if c == C]
        # print ids
        
        result = []
        close = 0
        for idx, c in enumerate(S):
            tmp = abs(idx - ids[close])
            right = abs(idx - ids[close+1]) if close+1 < len(ids) else tmp
            if right < tmp:
                close+=1
                tmp = right
            result.append(tmp)
        return result
