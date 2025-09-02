from collections import deque
import sys

input = sys.stdin.readline

def bfs(x,y):
	q = deque([(x,y)])

	while q:
		curX, curY = q.popleft()
		
		for i in range(4):
			nx = curX+dx[i]
			ny = curY+dy[i]
			
			if nx < 0 or nx >= n or ny < 0 or ny >= m:
				continue
			
			if ice[nx][ny] > 0 and not visited[nx][ny]:
				visited[nx][ny] = True
				q.append((nx,ny))
		
def meltIce():
    # 'melt' 배열을 매번 새로 만들 필요 없이, '빙산이 있는 좌표'만 관리
    melt_positions = []  # (녹을 빙산의 좌표, 해당 좌표에서 녹을 얼음의 양) 저장
    for i in range(n):
        for j in range(m):
            if ice[i][j] > 0:
                cnt = 0
				
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    
                    if 0 <= nx < n and 0 <= ny < m and ice[nx][ny] == 0:
                        cnt += 1
                if cnt > 0:  # (현재 좌표, 녹을 얼음의 양) 저장
                    melt_positions.append((i, j, cnt))

    # 순회하면서 좌표 별로 녹을 얼음의 양만큼 빙산을 녹임
    for x, y, melt_amount in melt_positions:
        ice[x][y] = max(0, ice[x][y] - melt_amount)  #음수 방지	

	
n,m = map(int,input().split())

dx = [1,-1,0,0]
dy = [0,0,1,-1]
year = 0
continent = 0
ice = []

melt = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
	
for _ in range(n):
	ice.append(list(map(int,input().split())))
			
while True:
	# 빙산이 쪼개지지 않고 모두 녹은 경우 0 출력 후 종료
	if max(map(max,ice)) == 0:
		print(0)
		break

	for i in range(n):
		for j in range(m):
			if ice[i][j] > 0 and not visited[i][j]:
				visited[i][j] = True
				continent += 1
				bfs(i,j)
				
	meltIce()
	
    # 빙산이 2덩어리 이상 쪼개진 경우 출력 후 종료
	if continent >= 2:
		print(year)
		break
				
	melt = [[0]*m for _ in range(n)]
	visited = [[False]*m for _ in range(n)]
	continent = 0
	year += 1