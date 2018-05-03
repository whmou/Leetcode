class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        lr = 0
        ud = 0
        for move in moves:
            if move == 'L':
                lr -= 1
            elif move == 'R':
                lr += 1
            elif move == 'U':
                ud += 1
            elif move == 'D':
                ud -= 1
        return lr == 0 and ud == 0
