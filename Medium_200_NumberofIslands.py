class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        M=len(grid)
        N=len(grid[0])
		
        islandNum=0
    
        for i in range(M):
            for j in range(N):
                if grid[i][j] == '1':
                    islandNum=islandNum+1
                    grid = self.changefunc(grid,i,j)
                    
        return islandNum

    def changefunc(self, matrix, x, y):

        matrix[x][y] = '#'
        
        #Up
        if ((x-1)>=0) and (matrix[(x-1)][y]=='1'):
            matrix=self.changefunc(matrix,x-1,y)
  
        #left    
        if ((y-1)>=0) and (matrix[x][(y-1)]=='1'):
            matrix=self.changefunc(matrix,x,y-1)
        
        #right  
        if (y+1)<len(matrix[0]) and (matrix[x][(y+1)]=='1'):
            matrix=self.changefunc(matrix,x,y+1)
        #down    
        if (x+1)<len(matrix) and (matrix[(x+1)][y]=='1'): 
            matrix=self.changefunc(matrix,x+1,y)
        
        return matrix