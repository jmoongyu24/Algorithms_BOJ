import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(input().strip()) for _ in range(N)]
dist = [[0] * M for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    x -= 1
    y -= 1
    q = deque([(x, y)])
    maze[x][y] = '0'
    dist[x][y] = 1
    
    while q:
        curX, curY = q.popleft()

        for i in range(4):
            nx = curX + dx[i]
            ny = curY + dy[i]

            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == '1':
                    maze[nx][ny] = '0'
                    dist[nx][ny] = dist[curX][curY] + 1
                    q.append((nx, ny))
            else:
                continue

    return dist[N-1][M-1]

print(bfs(1,1))