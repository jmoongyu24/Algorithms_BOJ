import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a<b:
        parent[b]=a
    else:
        parent[a]=b

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

V, E = map(int, input().split())

parent = [i for i in range(V+1)]
graph = []

for _ in range(E):
    A, B, C = map(int, input().split())
    graph.append((A, B, C))

graph.sort(key=lambda x: x[2])  # 간선 비용을 기준으로 오름차순 정렬
cost = 0

for edge in graph:
    a, b, c = edge

    if find_parent(a) != find_parent(b):    # 두 정점이 다른 그룹이면 같은 그룹으로 합치고, 현재 간선을 MST에 추가 (여기서는 비용만)
        union_parent(a, b)
        cost += c

print(cost)