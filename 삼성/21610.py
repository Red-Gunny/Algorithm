import sys

input = sys.stdin.readline

N, M = map(int, input().split())    # N은 정사각형 크기 / M 이동정보 개수
graph = [list(map(int, input().split())) for _ in range(N)]

# 이동정보
dy = [0, -1, -1, -1, 0, 1, 1, 1]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]

cloud = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]    #초기 구름 리스트


# 구름을 이동시킴
def move_cloud(cloud, move_idx, move_cnt, visit):
    for i, location in enumerate(cloud):    # 기존 구름들에 대하여
        for j in range(move_cnt):  # 움직이는 횟수
            cloud[i][0] += dy[move_idx - 1]
            if cloud[i][0] == N:
                cloud[i][0] = 0
            elif cloud[i][0] == -1:
                cloud[i][0] = N-1
            cloud[i][1] += dx[move_idx - 1]
            if cloud[i][1] == N:
                cloud[i][1] = 0
            elif cloud[i][1] == -1:
                cloud[i][1] = N-1
            if j == move_cnt - 1:
                visit[cloud[i][0]][cloud[i][1]] = True
    return visit

# 비를 뿌림
def do_rain(cloud):
    for yPos, xPos in cloud:
        graph[yPos][xPos] += 1

# 대각선
def water_copy(cloud):
    dy = [-1, 1, 1, -1]
    dx = [1, 1, -1, -1]
    for yPos, xPos in cloud:
        plus_amount = 0
        for i in range(4):
            move_y, move_x = yPos + dy[i], xPos + dx[i]
            if not 0 <= move_y < N or not 0 <= move_x < N:
                continue
            if graph[move_y][move_x] != 0:
                plus_amount += 1
        graph[yPos][xPos] += plus_amount    # 해당 구름 위치에 물을 증가시킴

def get_cloud_area(cloud, visit):
    created_area = []
    sum = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] >= 2 and not visit[i][j]:
                created_area.append([i, j])
                graph[i][j] -= 2
            sum += graph[i][j]
    return created_area, sum

sum = 0
for _ in range(M):
    dir, amount = map(int, input().split())
    visit = [[False]*N for _ in range(N)]
    visit = move_cloud(cloud, dir, amount, visit)  # 구름 이동 (N^2)
    do_rain(cloud)                  # 비 뿌림 (N^2)
    water_copy(cloud)               # 대각선 조사 후 구름 위치의 물을 증가시킴
    created, sum = get_cloud_area(cloud, visit) # 새로운 구름 영역을 만듬 (N^2)
    cloud.clear()                   # 기존 구름 초기화
    cloud = created.copy()     #created.copy()          # 구름을 복사
print(sum)
