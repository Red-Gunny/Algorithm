import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
graph = [list(input()) for _ in range(N)]

visit_none = [[0]*N for _ in range(N)]
visit_yes = [[0]*N for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def bfs_none(start_x, start_y, RGB_value):
    q = deque()
    q.append((start_x, start_y))
    while q:        # 큐 안에 들어있으면 계속 진행
        xPos, yPos = q.popleft()        # 큐에서 하나 뺸다.
        for i in range(4):                 # 그래프니까 4방 탐색
            newX = xPos + dx[i]             # 다음 좌표
            newY = yPos + dy[i]
            if 0<=newX<N and 0<=newY<N and RGB_value == graph[newY][newX]:         # 좌표가 그래프 범위 이내 && 이전 RGB랑 일치
                if visit_none[newY][newX] == 0:
                    visit_none[newY][newX] = 1           # 방문했다 기록
                    q.append((newX, newY))          # 큐에 삽입

def bfs_yes(start_x, start_y, RGB):
    q = deque()
    q.append((start_x, start_y))
    while q:        # 큐 안에 들어있으면 계속 진행
        xPos, yPos = q.popleft()        # 큐에서 하나 뺸다.
        for i in range(4):                 # 그래프니까 4방 탐색
            newX = xPos + dx[i]             # 다음 좌표
            newY = yPos + dy[i]
            if 0<=newX<N and 0<=newY<N :         # 좌표가 그래프 범위 이내 && 이전 RGB랑 일치
                if RGB == True and (graph[newY][newX] == 'R' or graph[newY][newX]=='G'):
                    if visit_yes[newY][newX] == 0:
                        visit_yes[newY][newX] = 1           # 방문했다 기록
                        q.append((newX, newY))          # 큐에 삽입
                if RGB == False :
                    if graph[newY][newX] == 'B':
                        if visit_yes[newY][newX] == 0:
                            visit_yes[newY][newX] = 1
                            q.append((newX, newY))

none_result = 0
for i in range(N):
    for j in range(N):
        if visit_none[i][j] == 0:
            none_result += 1
            bfs_none(j, i, graph[i][j])

yes_result = 0
for i in range(N):
    for j in range(N):
        if visit_yes[i][j] == 0:
            if graph[i][j] == 'B':
                yes_result+=1
                bfs_yes(j, i, False)
            else :
                yes_result+=1
                bfs_yes(j, i, True)

print(str(none_result) + " " + str(yes_result))