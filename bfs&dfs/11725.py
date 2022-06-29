import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    e1, e2 = map(int, input().split())
    graph[e1].append(e2)
    graph[e2].append(e1)

distance = [-1]*(N+1)
result = [-1]*(N+1)

def bfs(start):
    q = deque()
    q.append(start)     # bfs 시작 노드
    result[start] = start
    while q:
        now = q.popleft()       # 1이 나와
        for next in graph[now]:
            if result[next] != -1:    # 이미 방문한 이력이 있음
                continue
            result[next] = now
            q.append(next)      # 큐에 삽입

bfs(1)

for i in range(2, N+1):
    print(result[i])
