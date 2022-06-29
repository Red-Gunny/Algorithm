import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
x, y= map(int, input().split())
m = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(m):
    first, second = map(int, input().split())
    graph[first].append(second)
    graph[second].append(first)

visited = [False]*(N+1)
notFind = True

def bfs(start):
    que = deque()
    que.append((start, 0))
    visited[start]=True
    while que:
        cur_node, cur_weight = que.popleft()
        if cur_node == y:           # 찾았다.
            print(cur_weight)
            global notFind
            notFind = False
            break
        for data in graph[cur_node]:        # 인접 노드들
            if not visited[data]:
                visited[data] = True
                que.append((data, cur_weight+1))

bfs(x)

if notFind:
    print(-1)