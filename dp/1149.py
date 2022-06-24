import sys
input = sys.stdin.readline
N = int(input())

graph = [[] for _ in range(N)]

for i in range(N):
    R, G, B = map(int, input().split())
    graph[i].append(R)
    graph[i].append(G)
    graph[i].append(B)

for i in range(1, len(graph)):
    graph[i][0] = min(graph[i-1][1], graph[i-1][2]) + graph[i][0]
    graph[i][1] = min(graph[i-1][0], graph[i-1][2]) + graph[i][1]
    graph[i][2] = min(graph[i-1][0], graph[i-1][1]) + graph[i][2]

print(min(graph[N-1][0], graph[N-1][1], graph[N-1][2]))