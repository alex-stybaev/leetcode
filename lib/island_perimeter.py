class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        perimeter = 0
        sizeY = len(grid)
        sizeX = len(grid[0])
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == 0:
                    continue
                current = 0
                if i == 0 or grid[i-1][j] == 0 :
                    current += 1
                if i == sizeY-1 or grid[i+1][j] == 0 :
                    current += 1
                if j == 0 or grid[i][j-1] == 0 :
                    current += 1
                if j == sizeX-1 or grid[i][j+1] == 0 :
                    current += 1
                perimeter += current
        return perimeter

list = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]


list1 = [[]]

s = Solution()

print(s.islandPerimeter(list1))