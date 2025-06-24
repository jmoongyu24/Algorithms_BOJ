import sys
from collections import deque

input=sys.stdin.readline

n,m=map(int, input().split())
picture=[list(map(int, input().split())) for _ in range(n)]

result=0
cnt=0

dx=[1,-1,0,0]
dy=[0,0,1,-1]

visited=[[False]*m for _ in range(n)]

def bfs(x, y):
    curArea=1
    visited[x][y]=True
    q=deque([(x,y)])

    while q:
        curX, curY=q.popleft()

        for i in range(4):
            nx=curX+dx[i]   #y축
            ny=curY+dy[i]   #x축

            # 다음에 방문할 ny(x축), nx(y축)의 값이 picture를 벗어나면 continue 
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            
            # 다음에 방문할 picture가 아직 방문되지 않았고, 그림이 그려져있다면 방문 처리 후 덱에 append
            if not visited[nx][ny] and picture[nx][ny]==1:
                visited[nx][ny]=True
                q.append((nx,ny))
                curArea+=1

    return curArea

for i in range(n):
    for j in range(m):
        # 현재 위치가 아직 방문되지 않았고, 그림이 그려져있다면 bfs 진행
        if picture[i][j]==1 and not visited[i][j]:
            cnt+=1
            result=max(result, bfs(i,j))

print(cnt)
print(result)