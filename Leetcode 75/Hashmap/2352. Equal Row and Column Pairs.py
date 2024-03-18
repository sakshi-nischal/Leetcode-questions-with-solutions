class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        grid_hashmap = {}
        n = len(grid)
        for r in range(n):
            row = tuple(grid[r])
            grid_hashmap[row] = grid_hashmap.get(row,0)+1
        for c in range(n):
            column = tuple([grid[r][c] for r in range(n)])
            count += grid_hashmap.get(column,0)
        return count
