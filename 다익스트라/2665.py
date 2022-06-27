import heapq

INF = int(1e9)
n = int(input())
graph = []
for i in range(n):
    graph_line = list(map(int, input()))
    graph.append(graph_line)

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

distance = [[INF]*(n+1) for _ in range(n+1)]

def bfs():
    global cost
    q = []
    heapq.heappush(q, (0, 0, 0))    # cost / xPos / yPos
    distance[0][0] = 0
    while q:
        now_cost, nowX, nowY = heapq.heappop(q)
        for i in range(4):
            next_x = nowX + dx[i]
            next_y = nowY + dy[i]
            if 0<= next_x < n and 0 <= next_y < n:
                if graph[next_y][next_x] == 1:
                    cost = distance[nowY][nowX]
                elif graph[next_y][next_x] == 0:
                    ost = distance[nowY][nowX] + 1
                if distance[next_y][next_x] > ost:
                    distance[next_y][next_x] = cost
                    heapq.heappush(q, (cost, next_x, next_y))


bfs()

#print(distance)
print(distance[n-1][n-1])