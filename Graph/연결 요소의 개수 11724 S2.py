import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
stack = []
count = 0

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for v in range(1, N + 1):
    if visited[v]:
        continue
    if not visited[v]:
        visited[v] = True
        stack.append(v)
        count += 1

        while stack:
            curNode = stack.pop()

            for nextNode in graph[curNode]:
                if not visited[nextNode]:
                    visited[nextNode] = True
                    stack.append(nextNode)

print(count)