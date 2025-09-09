import sys
input = sys.stdin.readline

V = int(input())
E = int(input())
graph = [[i] for i in range(V+1)]

for _ in range(E):
    s,e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

count = 0
visited = [False] * (V+1)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            global count
            count += 1

dfs(1)
print(count)