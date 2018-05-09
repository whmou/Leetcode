class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        num_1 = 0
        adj = 0
        for id1, l in enumerate(grid):
            for id2, i in enumerate(l):
                if i == 1:
                    num_1 += 1
                    if id2 + 1 < len(l) and l[id2 + 1] == 1:
                        adj += 1
                    if id2 - 1 >= 0 and l[id2 - 1] == 1:
                        adj += 1
                    if id1 - 1 >= 0 and grid[id1 - 1][id2] == 1:
                        adj += 1
                    if id1 + 1 < len(grid) and grid[id1 + 1][id2] == 1:
                        adj += 1
        return 4 * num_1 - adj
