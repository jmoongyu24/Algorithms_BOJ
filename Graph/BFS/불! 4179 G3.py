import sys
from collections import deque

h, w = map(int, sys.stdin.readline().split())

maze = [list(sys.stdin.readline().strip()) for _ in range(h)]
dist_f = [[-1 for _ in range(w)] for _ in range(h)]
dist_j = [[-1 for _ in range(w)] for _ in range(h)]

q_f = deque()
q_j = deque()

for y in range(h):
    for x in range(w):
        if maze[y][x] == 'J':
            q_j.append((x, y))
            dist_j[y][x] = 0
        elif maze[y][x] == 'F':
            q_f.append((x, y))
            dist_f[y][x] = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs_f():
    while q_f:
        x, y = q_f.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= ny < h and 0 <= nx < w:
                if maze[ny][nx] != '#' and dist_f[ny][nx] == -1:
                    q_f.append((nx, ny))
                    dist_f[ny][nx] = dist_f[y][x] + 1

bfs_f()

def bfs_j():
    while q_j:
        x, y = q_j.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 지훈이 탈출
            if 0 > ny or ny >= h or 0 > nx or nx >= w:
                return dist_j[y][x] + 1
            
            # 다음 위치가 통로이고, 방문하지 않았으며, 불보다 먼저 도달할 수 있는 경우
            if maze[ny][nx] == '.' and dist_j[ny][nx] == -1:
                if dist_f[ny][nx] == -1 or dist_f[ny][nx] > dist_j[y][x] + 1:
                    q_j.append((nx, ny))
                    dist_j[ny][nx] = dist_j[y][x] + 1
    return "IMPOSSIBLE"


print(bfs_j())

"""
# 메모리 초과 코드
import sys
from collections import deque
input = sys.stdin.readline
inf = 9999

R, C = map(int, input().split())
maze = [list(input().strip()) for _ in range(R)]
visited_j = [[False] * C for _ in range(R)]
visited_f = [[False] * C for _ in range(R)]
dist_j = [[inf] * C for _ in range(R)]
dist_f = [[0] * C for _ in range(R)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs_f(x, y):
    q = deque([(x, y)])
    visited_f[x][y] = True
    dist_f[x][y] = 0
    
    while q:
        curX, curY = q.popleft()
        
        for i in range(4):
            nx = curX + dx[i]
            ny = curY + dy[i]
            
            if 0 <= nx < R and 0 <= ny < C:
                # 벽이거나 이미 불난 곳이면 패스
                if maze[nx][ny] == '#' or visited_f[nx][ny]:
                    continue

                dist_f[nx][ny] = dist_f[curX][curY] + 1
                visited_f[nx][ny] = True
                q.append((nx, ny))

def bfs_j(x, y):
    q = deque([(x, y)])
    visited_j[x][y] = True
    dist_j[x][y] = 0
    
    while q:
        curX, curY = q.popleft()
        
        for i in range(4):
            nx = curX + dx[i]
            ny = curY + dy[i]
            
            if 0 <= nx < R and 0 <= ny < C:
                # 벽이거나 이미 불난 곳이면 패스
                if maze[nx][ny] == '#' or dist_j[curX][curY] + 1 >= dist_f[nx][ny]:
                    continue

                # 통로이고 불이 아직 안 번진 곳이면
                if maze[nx][ny] == '.':
                    visited_j[nx][ny] = True
                    dist_j[nx][ny] = dist_j[curX][curY] + 1
                    q.append((nx, ny))
                    
x_j, y_j, x_f, y_f = 0, 0, 0, 0

for i in range(R):
    for j in range(C):
        if maze[i][j] == 'J':
            x_j = i
            y_j = j
        if maze[i][j] == 'F':
            x_f = i
            y_f = j

# 불 먼저 지르고            
bfs_f(x_f, y_f)
# 지훈이가 지나가기
# 불보다 늦으면 inf, 그렇지 않으면 지나감. 지나간 곳 중 탈출했다면 최단경로의 값 찾기
bfs_j(x_j, y_j)
result = inf

for i in range(R):
    for j in range(C):
        if i == 0 or i == R-1 or j == 0 or j == C-1:
            result = min(result, dist_j[i][j])

if result == inf:
    print("IMPOSSIBLE")
else:
    print(result+1)
"""