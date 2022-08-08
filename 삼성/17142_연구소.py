import itertools
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

# virus_list는 (ypos, xPos)의 리스트
def bfs(virus_list, visited) :
    q = deque()
    empty_cnt = 0
    max_time = 0
    for vy, vx in virus_list:
        q.append((vy, vx, 0, False))
        visited[vy][vx] = True
    while q:
        cy, cx, ct, no_virus = q.popleft()
        if no_virus:
            max_time = max(max_time, ct)
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if not 0 <= ny < N or not 0 <= nx < N:  # 그래프 범위 밖
                continue
            if graph[ny][nx] == 1:
                continue
            if visited[ny][nx]:
                continue
            visited[ny][nx] = True
            if graph[ny][nx] == 2:
                q.append((ny, nx, ct+1, False))
            else :
                q.append((ny, nx, ct+1, True))
                empty_cnt += 1
    if two_cnt + one_cnt + empty_cnt < N*N :
        max_time = -1
    return max_time


virus_q = deque()

two_cnt = 0
one_cnt = 0

for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            virus_q.append((i, j))      # 바이러스가 있는 곳을 넣었다
            two_cnt += 1
        if graph[i][j] == 1:
            one_cnt += 1

answer = int(1e9)

for viruses in itertools.combinations(virus_q, M):
    visit_graph = [[False] * N for _ in range(N)]
    time = bfs(viruses, visit_graph)

    if time == -1:
        continue
    answer = min(answer, time)


if answer == int(1e9):
    print(-1)
else :
    print(answer)