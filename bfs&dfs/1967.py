import sys
import heapq

sys.setrecursionlimit(100000)
input = sys.stdin.readline
INF = int(1e9)

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    parent, child, weight = map(int, input().split())
    graph[parent].append((child, weight))
    graph[child].append((parent, weight))


result = 0
idx_record = 0
def dfs(node, weight):
    if visited[node] != -1:
        return
    visited[node] = weight
    global result
    #result = max(result, weight)
    if result < weight:
        result = weight
        global idx_record
        idx_record = node
    for adj in graph[node]:
        dfs(adj[0], weight+adj[1])


visited = [-1] * (N + 1)
dfs(1, 0)
#print(idx_record)
#print(result)
#input()
visited = [-1] * (N + 1)
dfs(idx_record, 0)
print(result)
