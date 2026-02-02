import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

picture = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    area = 1
    visited[x][y] = True
    q = deque([(x, y)])

    while q:
        curX, curY = q.popleft()

        for i in range(4):
            nx = curX + dx[i]
            ny = curY + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and picture[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    area += 1

    return area

count = 0
max_area = 0

for i in range(n):
    for j in range(m):
        if picture[i][j] == 1 and not visited[i][j]:
            count += 1
            max_area = max(max_area, bfs(i, j))

print(count)
print(max_area)