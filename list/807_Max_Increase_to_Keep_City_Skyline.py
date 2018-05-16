class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        sum = 0
        for l_id, l in enumerate(grid):
            for b_id, b in enumerate(l):
                tmp_col = list()
                for i in range(0, len(grid)):
                    tmp_col.append(grid[i][b_id])
                sum += (min(max(l), max(tmp_col)) - b)
        return sum
