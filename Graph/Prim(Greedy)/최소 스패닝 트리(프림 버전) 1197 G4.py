import sys
from heapq import heappop, heappush

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    A, B, C = map(int, input().split())
    graph[A].append((C, B))
    graph[B].append((C, A))

def prim(start):
    visited = [False] * (V + 1)
    pq = []
    heappush(pq, (0, start))
    total_cost = 0
    count = 0

    while pq and count < V:
        curCost, curNode = heappop(pq)

        if visited[curNode]:
            continue

        visited[curNode] = True
        total_cost += curCost
        count += 1

        for nextCost, nextNode in graph[curNode]:
            if not visited[nextNode]:
                heappush(pq, (nextCost, nextNode))

    return total_cost

print(prim(1))