from collections import deque
import sys

input = sys.stdin.readline

# 이동 방향 설정용
dx = [1,-1,0,0]
dy = [0,0,1,-1]

n, m = map(int,input().strip().split())
graph = []

# 미로 방문 여부 표시
visited = [[False] * m for _ in range(n)]
# (1,1)로부터의 거리 기록
dist=[[0] * m for _ in range(n)]

for _ in range(n):
	graph.append(list(input().strip()))
	
# (0,0) (= 실제 미로에서는 1,1) 방문 표시
q=deque([(0,0)])
visited[0][0] = True
dist[0][0] = 1

while q:
	curX,curY = q.popleft()
	
	for i in range(4):
		nx = curX + dx[i]
		ny = curY + dy[i]
		
        # 만약 다음 위치가 미로를 벗어나면 continue
		if nx < 0 or nx >= n or ny < 0 or ny >= m:
			continue
		
        # 만약 다음 위치를 방문하지 않았고, 다음 위치의 미로가 1이라면 방문 표시 후 큐에 append
		if not visited[nx][ny] and graph[nx][ny] == '1':
			visited[nx][ny] = True
			dist[nx][ny] = dist[curX][curY]+1
			q.append((nx,ny))

print(dist[n-1][m-1]) 