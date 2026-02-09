import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
parent = [0] * (N + 1)

for _ in range(N - 1):
    s, e = map(int,input(). split())
    graph[s].append(e)
    graph[e].append(s)

def dfs(v):
    visited[v] = True
    
    for nextNode in graph[v]:
        if not visited[nextNode]:
            parent[nextNode] = v
            dfs(nextNode)

dfs(1)

for v in range(2, N + 1):
    print(parent[v])