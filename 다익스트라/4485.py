import heapq
import sys
INF = int(1e9)
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def dijkstra(start_x, start_y):
    q = []
    heapq.heappush(q, (table[0][0], start_x, start_y))
    distance[start_y][start_x] = table[start_y][start_x]
    while q:
        dist, now_x, now_y = heapq.heappop(q)       # 5, 0, 0
        if dist > distance[now_y][now_x] :
            continue
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                cost = dist + table[ny][nx]
                if distance[ny][nx] > cost :
                    distance[ny][nx] = cost
                    heapq.heappush(q, (cost, nx, ny))
    return distance
N=-1
idx=1
while N != 0 :
    N = int(input())
    if N == 0:
        break
    table = [list(map(int, input().split())) for _ in range(N)]
    distance = [[INF] * N for _ in range(N)]
    dijkstra(0,0)
    result = distance[N-1][N-1]
    print("Problem " + str(idx) + ": " + str(result))
    idx+=1