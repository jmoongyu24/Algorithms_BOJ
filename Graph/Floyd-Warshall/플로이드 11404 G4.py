import sys
input = sys.stdin.readline
inf = 999999

n = int(input())
m = int(input())
dist = [[inf] * 101 for _ in range(101)]

for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a][b] = min(dist[a][b], c)

for k in range(1, n + 1):   # 중간에 거쳐갈 노드를 바깥 for문으로 처리
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])   #  if(d[i][k] + d[k][j] < d[i][j]) d[i][j] = d[i][k] + d[k][j] 이렇게 하는게 더 빠르다고 함

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if dist[i][j] == inf or i == j:
            print(0, end = ' ')
        else:
            print(dist[i][j], end = ' ')
    print()