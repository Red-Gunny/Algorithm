import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
graph = [[0]*N for _ in range(N)]   # 자리
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]
empty_seat = set()  # 해시
for i in range(N):
    for j in range(N):
        empty_seat.add((i, j))
like_db = {}        # id를 키값으로 좋아하는 사람 리스트 저장.

for _ in range(N*N):
    id, like1, like2, like3, like4 = map(int, input().split())
    like_db[id] = (like1, like2, like3, like4)

for id in like_db.keys():
    love_and_empty_db = defaultdict(list)
    max_cnt = 0
    for y, x in empty_seat:  # 비어있는 칸들에 대하여
        love_cnt, empty_cnt = 0, 0  # 카운팅 변수 초기화
        if graph[y][x] != 0:
            continue
        for i in range(4):
            adj_y, adj_x = y + dy[i], x + dx[i]  # 인접 자리 탐문해보겠음
            if not 0 <= adj_y < N or not 0 <= adj_x < N:  # 그래프 범위 벗어날 때 예외 처리
                continue
            if graph[adj_y][adj_x] in like_db[id]:  # 좋아하는 애가 해당 위치에 있으면
                love_cnt += 1  # 좋아하는 - 카운팅변수++
            if graph[adj_y][adj_x] == 0:  # 비어있으면
                empty_cnt += 1  # 비어있는 - 카운팅 변수++
        love_and_empty_db[(love_cnt, empty_cnt)].append((y, x))
    candidate_list = sorted(love_and_empty_db.items(), reverse=True)
    most, location = candidate_list[0]
    location.sort()
    suc_y, suc_x = location[0][0], location[0][1]
    graph[suc_y][suc_x] = id

sum = 0
for i in range(N):
    for j in range(N):
        satisfied = 0
        for k in range(4):
            adj_y, adj_x = i + dy[k], j + dx[k]
            if not 0 <= adj_y < N or not 0 <= adj_x < N:  # 그래프 예외조건
                continue
            if graph[adj_y][adj_x] in like_db[graph[i][j]]:
                satisfied += 1
        if satisfied == 0:
            continue
        mid = 1
        for k in range(satisfied-1):
            mid *= 10
        sum += mid
print(sum)