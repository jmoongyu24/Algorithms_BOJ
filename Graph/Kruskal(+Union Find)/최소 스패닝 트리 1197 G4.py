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
        parent[x] = find_parent(parent[x])  # 경로 압축
        #return find_parent(parent[x]) - 재귀적으로 탐색하지만, 부모의 값을 갱신하지 않으므로 트리의 높이가 커짐
    return parent[x]
    # return x
    
V, E = map(int, input().split())

parent = [i for i in range(V+1)]
graph = []

for _ in range(E):
    A, B, C = map(int, input().split())
    graph.append((A, B, C))

graph.sort(key=lambda x: x[2])
cost = 0

for edge in graph:
    a, b, c = edge
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        cost += c

print(cost)