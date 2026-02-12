import sys
from collections import defaultdict
import heapq
INF = 987654321
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

dist = [INF] * (n+1)    # 각 노드 별 거리 초기화
prev_node = [0] * (n+1) # 현재 노드 도착 직전 노드 기록용 리스트

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        curDist, curNode = heapq.heappop(q)

        if dist[curNode] < curDist:
            continue

        for nextNode, nextDist in graph[curNode]:
            if dist[nextNode] > curDist + nextDist:
                dist[nextNode] = curDist + nextDist
                prev_node[nextNode] = curNode
                heapq.heappush(q, (curDist + nextDist, nextNode))

dijkstra(start)
print(dist[end])

# 경로 복원 코드
path = [end]
cur = end

# 현재 노드가 시작 노드가 될 때까지 거슬러 올라감
while cur != start:
    cur = prev_node[cur]
    path.append(cur)

path.reverse()

print(len(path))
print(' '.join(map(str, path)))