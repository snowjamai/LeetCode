from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        mv_x=[0,1,0,-1]
        mv_y=[1,0,-1,0]
        cnt = 0
        Q = deque()
        
        W = len(grid[0])
        H = len(grid)
        
        for h in range(H):
            for w in range(W):
                if visit[h][w] == 0 and grid[h][w] == '1':
                    cnt += 1
                    visit[h][w] = 1
                    Q.append([w, h])
                    
                    while len(Q):
                        tmp = Q.popleft()
                        
                        for i in range(4):
                            nx = tmp[0] + mv_x[i]
                            ny = tmp[1] + mv_y[i]
                            
                            if nx < 0 or nx >= W or ny < 0 or ny >= H:
                                continue
                            else:
                                if grid[ny][nx] == '1' and visit[ny][nx] == 0:
                                    visit[ny][nx] = 1
                                    Q.append([nx,ny])
                                    
        print(visit)
        return cnt
                                    
                        
                        
        
       
                    
                    
                    
                    
        