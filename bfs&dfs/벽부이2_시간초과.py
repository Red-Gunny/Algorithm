import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

visited = [[[0]*M for _ in range(N)] for _ in range(K+1)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

q = deque()
visited[0][0][0] = 1
visited[1][0][0] = 1
q.append((0, 0, 0))
while q:
    cy, cx, crash_cnt = q.popleft()
    #print(q)
    for i in range(4):
        ny, nx = cy+dy[i], cx+dx[i]
        if not 0 <= ny < N or not 0 <= nx < M:  # 그래프 범위 벗어남
            continue
        if crash_cnt < K:
            if visited[crash_cnt][ny][nx] != 0: # 이미 방문 했어
                continue
            if graph[ny][nx] == 0:  # 다음에 갈 곳이 0이야 -> No Problem
                visited[crash_cnt][ny][nx] = visited[crash_cnt][cy][cx] + 1
                q.append((ny, nx, crash_cnt))
            elif graph[ny][nx] == 1:    # 다음에 갈 곳이 1이야 -> 부셔야대
                visited[crash_cnt+1][ny][nx] = visited[crash_cnt][cy][cx] + 1   # K까지 ㄱㄴ
                q.append((ny, nx, crash_cnt+1))
        else:    # 이미 K에 도달했어. -> 1로는 못가욜~ 0이면 갈수 있어.
            if visited[crash_cnt][ny][nx] != 0:
                continue
            if graph[ny][nx] == 0:      # 다음에 갈 곳이 0이야
                visited[crash_cnt][ny][nx] = visited[crash_cnt][cy][cx] + 1
                q.append((ny, nx, crash_cnt))
            elif graph[ny][nx] == 1:    # 다음에 갈 곳이 1이야...
                visited[K][ny][nx] = -1


answer = int(1e9)
for i in range(K+1):
    if visited[i][N-1][M-1] == 0:
        continue
    else :
        answer = min(answer, visited[i][N-1][M-1])

print(answer if answer != int(1e9) else -1)
