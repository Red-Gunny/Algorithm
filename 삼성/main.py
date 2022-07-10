import sys
from collections import deque
import heapq

input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
baby_y, baby_x = 0, 0         # 현재 아기 상어의 위치
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            baby_y, baby_x = i, j
            break
# 입력 정보 파싱 완료

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

baby_size, mommy_time = 2, 0
eaten_cnt = 0
feed_heap = []

def bfs(start_y, start_x):
    global baby_size, eaten_cnt
    visited = [[0]*N for _ in range(N)]
    q = deque()
    q.append((0, start_y, start_x))
    visited[start_y][start_x] = 1
    before_dist = 0
    while q:
        dist, cur_y, cur_x = q.popleft()
        if dist != before_dist: # 거리가 달라졌음 (하나의 waveFront) 들어있는지 확인 필
            if feed_heap: # 뭔가가 들어있어. - 확인해야 함.
                feed_y, feed_x, feed_dist = heapq.heappop(feed_heap)    # 잡았다 요놈
                global baby_y, baby_x, mommy_time
                graph[baby_y][baby_x] = 0
                baby_y, baby_x = feed_y, feed_x   # 아기 복어 이동
                mommy_time += feed_dist         # 거리 증가
                eaten_cnt += 1                  # 먹는 카운팅 증가
                graph[baby_y][baby_x] = 0         # 먹었으니까 그래프 0으로 변경
                is_baby_growth(baby_size, eaten_cnt)    # 아가 성장?
                return True
        for i in range(4):
            next_y, next_x = cur_y + dy[i], cur_x + dx[i]   # 그 다음 좌표
            if not 0 <= next_y < N or not 0 <= next_x < N or visited[next_y][next_x]:  # 그래프 범위 초과했으면 고려할 필요도 없어~
                continue
            if graph[next_y][next_x] > baby_size:   # 아기상어보다 크기가 크면 무시
                continue
            if 0 < graph[next_y][next_x] < baby_size:   # 아기상어가 먹을 수 있으면
                heapq.heappush(feed_heap, (next_y, next_x, dist+1))
            q.append((dist+1, next_y, next_x))  # 큐에 삽입
            visited[next_y][next_x] = 1             # 나(Me) 갔습니다,
        before_dist = dist
    return False    # 씨발 아무것도 먹지 못했어

def is_baby_growth(size, cnt):
    if size == cnt:
        global baby_size, eaten_cnt
        baby_size += 1
        eaten_cnt = 0
        return True
    return False

while True:
    result = bfs(baby_y, baby_x)
    feed_heap.clear()   # 먹이 힙 초기화.
    if not result:
        print(mommy_time)
        exit(0)
