import sys
from collections import deque

input = sys.stdin.readline

def challenge(west, east):
    graph = [[0]*(east+1) for _ in range(east+1)]
    for i in range(1, west+1):
        for j in range(1, east+1):
            if i == 1:
                graph[i][j] = j
                continue
            if i == j:
                graph[i][j] = 1
            else :
                if j > i:
                    graph[i][j] = graph[i-1][j-1] + graph[i][j-1]
    return graph[west][east]

N = int(input())
for _ in range(N):
    west, east = map(int, input().split())
    print(challenge(west, east))
