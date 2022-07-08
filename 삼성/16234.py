import sys
from collections import deque

input = sys.stdin.readline

N, L, R = map(int, input().split()) # N은 정사각형 사이즈 / L, R 인구 이동 조건
graph = [list(map(int ,input().split())) for _ in range(N)] # 그래프 파싱

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]  # 오른쪽 / 밑 / 왼쪽 / 위쪽


def bfs(yPos, xPos, visit):
    sum = 0
    nation_cnt = 0
    q = deque()
    q.append((yPos, xPos))  # 시작 좌표 삽입   - for Q
    visit_location.append((yPos, xPos))     # 시작 좌표 기록 (나중에 수정)
    sum += graph[yPos][xPos]    # 인구수 더함
    nation_cnt += 1             # 이동수 더함
    visit[yPos][xPos] = 1
    while q:
        cur_y, cur_x = q.popleft()
        for i in range(4):  # 인접 좌표 조사
            next_y, next_x = cur_y + dy[i], cur_x + dx[i]   # 인접 조사
            if 0 <= next_y < N and 0 <= next_x < N and visit[next_y][next_x] == 0:     # 그래프 이내면
                if L <= abs(graph[cur_y][cur_x] - graph[next_y][next_x]) <= R : # 인구 수 인접차가 이 정도면
                    global is_moved
                    is_moved = True
                    q.append((next_y, next_x))  # 큐에 삽입
                    visit_location.append((next_y, next_x))     # for 나중에 기록
                    visit[next_y][next_x] = 1   # 방문했다이거야
                    nation_cnt += 1             # 나라 수 더함
                    sum += graph[next_y][next_x]    # 인구수 더함
    return int(sum / nation_cnt)    # 각 개별 인구수.

is_moved = False
visit_location = []       # 방문 좌표 기록할 것임.
days = 0
while True:
    if not is_moved and days != 0:        # 이전날에 인구 이동이 없었으면
        print(days-1)
        exit(0)             # 종료~
    is_moved = False
    days += 1  # 날 수 증가
    visited = [[0] * N for _ in range(N)]  # 방문 기록 그래프
    for i in range(N):
        for j in range(N):
            if visited[i][j] != 0:      # 이미 수정했으면 스킵
                continue
            moved = bfs(i, j, visited)      # 국경 열리는지 검사
            for record_y, record_x in visit_location:       # 결과로 나온 모든 좌표에 대하여
                graph[record_y][record_x] = moved  # 바뀐거 기록
            visit_location.clear()      # 다 기록했으니까 지워~


