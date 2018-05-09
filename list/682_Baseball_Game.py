class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        sum = 0
        round_records = []
        for op in ops:
            points_this_round = 0
            if op == '+':
                points_this_round = round_records[-1] + round_records[-2]
            elif op == 'D':
                points_this_round = round_records[-1] * 2
            elif op == 'C':
                sum -= round_records.pop()
            else:
                points_this_round = int(op)
            if op != 'C':
                round_records.append(points_this_round)
            sum += points_this_round
        return sum
