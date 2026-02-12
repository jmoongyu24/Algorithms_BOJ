import sys
input = sys.stdin.readline
inf = 999999

n = int(input())
m = int(input())
dist = [[inf] * 101 for _ in range(101)]
nxt = [[0] * 101 for _ in range(101)]

for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a][b] = min(dist[a][b], c)
    nxt[a][b] = b

for i in range(1, n + 1):
    dist[i][i] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                nxt[i][j] = nxt[i][k]   # i -> j 경로에서 k를 거쳐가는 것이 좋다면 i의 다음 목적지는 k 노드

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if dist[i][j] == inf or i == j:
            print(0, end = ' ')
        else:
            print(dist[i][j], end = ' ')

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if dist[i][j] == inf or i == j:
            print(0)
            continue
        else:
            path = []
            cur = i     # 시작 위치 i 노드
            
            while cur != j:     # j 노드에 도달할 때까지
                path.append(cur)
                cur = nxt[cur][j]   # i->j 경로로 나아가면서 거치는 노드 계속 추가
            
            path.append(j)  # 목적지 노드 j 도착
            print(len(path), *path)