import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

visited = [[[0]*M for _ in range(N)] for _ in range(2)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

q = deque()
visited[0][0][0] = 1
visited[1][0][0] = 1
q.append((0, 0, False))
while q:
    cy, cx, is_crash = q.popleft()
    for i in range(4):
        ny, nx = cy+dy[i], cx+dx[i]
        if not 0 <= ny < N or not 0 <= nx < M:  # 그래프 범위 벗어남
            continue
        if is_crash:    # 이미 부셨어... -> 1로는 못가욜~ 0이면 갈수 있어.
            if visited[1][ny][nx] != 0:
                continue
            if graph[ny][nx] == 0:      # 다음에 갈 곳이 0이야
                visited[1][ny][nx] = visited[1][cy][cx] + 1
                q.append((ny, nx, is_crash))
            elif graph[ny][nx] == 1:    # 다음에 갈 곳이 0이야...
                visited[1][ny][nx] = -1
        else :  # 안 부셨지롱~
            if visited[0][ny][nx] != 0: # 이미 방문 했어
                continue
            if graph[ny][nx] == 0:  # 다음에 갈 곳이 0이야 -> No Problem
                visited[0][ny][nx] = visited[0][cy][cx] + 1
                q.append((ny, nx, is_crash))
            elif graph[ny][nx] == 1:    # 다음에 갈 곳이 1이야 -> 부셔야대
                visited[1][ny][nx] = visited[0][cy][cx] + 1
                q.append((ny, nx, True))


if visited[0][N-1][M-1] == 0 and visited[1][N-1][M-1] == 0:
    print(-1)
elif visited[0][N-1][M-1] != 0 and visited[1][N-1][M-1] != 0:
    print(min(visited[0][N-1][M-1], visited[1][N-1][M-1]))
else:
    print(max(visited[0][N-1][M-1], visited[1][N-1][M-1]))