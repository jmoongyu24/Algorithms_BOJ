from collections import deque
import sys

input = sys.stdin.readline
N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(1, N + 1):
    graph[i].sort()

visited_dfs = [False] * (N + 1)
stack = []

# 재귀 DFS
def dfs(v):
    visited_dfs[v] = True
    print(v, end= ' ')

    for nextNode in graph[v]:
        if not visited_dfs[nextNode]:
            dfs(nextNode)
"""
# 비재귀 DFS, 재귀형과 다르게 방문 순서가 다름. 스택 메모리 면에서 효율적임
def dfs(v):
    visited_dfs[v] = True
    print(v, end = ' ')
    stack.append(v)

    while stack:
        curNode = stack.pop()

        for nextNode in graph[curNode]:
            if not visited_dfs[nextNode]:
                visited_dfs[nextNode] = True
                print(nextNode, end = ' ')
                stack.append(nextNode)
"""

visited_bfs = [False] * (N + 1)
q = deque()

def bfs(v):
    visited_bfs[v] = True
    print(v, end = ' ')
    q.append(v)

    while q:
        curNode = q.popleft()

        for nextNode in graph[curNode]:
            if not visited_bfs[nextNode]:
                visited_bfs[nextNode] = True
                print(nextNode, end = ' ')
                q.append(nextNode)

dfs(V)
print()
bfs(V)