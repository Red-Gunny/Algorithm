import sys

input = sys.stdin.readline

def turn_left(cur_dir, i):
    return (cur_dir+i+1) % 4

N, M = map(int, input().split())    # N은 세로 / M은 가로
cur_y, cur_x, robot_dir = map(int, input().split())     # 로봇 위치 / 바라보는 방향
graph = [list(map(int, input().split())) for _ in range(N)]     # 지형지물
cleaned = [[0]*M for _ in range(N)]     # 청소했는지
result = 0

dy = [-1, 0, 1, 0]  # 북, 서, 남, 동 순
dx = [0, -1, 0, 1]

# 문제조건 -> 내 조건 보정
if robot_dir == 1:
    robot_dir = 3
elif robot_dir == 3:
    robot_dir = 1

while True:
    is_find = False
    # 시작 부분 and 왼쪽 탐색 중 찾았을 때
    if cleaned[cur_y][cur_x] == 0:
        result += 1  # 결과 카운팅 변수 ++
    cleaned[cur_y][cur_x] = 1  # 현재 위치 청소
    left_dir = robot_dir + 1  # 왼쪽 간보는 좌표계
    for i in range(4):
        # 탐문 시작
        if left_dir == 4:  # 왼쪽 간보는게 배열 벗어나려고하면
            left_dir = 0
        left_y, left_x = cur_y + dy[left_dir], cur_x + dx[left_dir]  # 바라보고 있는거 기준 왼쪽 좌표
        if cleaned[left_y][left_x] == 0 and graph[left_y][left_x] != 1:  # 청소 안했고, 벽 아니면
            robot_dir = turn_left(robot_dir, i)  # 현재 로봇 바라보는 방향 변경
            cur_y, cur_x = left_y, left_x  # 한칸 전진데스
            is_find = True  # 4번 돌았느데 못찾음 - 후진 때 사용
            break  # 4번 루프 탈출.
        else:  # 한번더 회전
            left_dir += 1  # 왼쪽 간보는 인덱스 1증가 시킴
    if not is_find:  # 못찾았음 - 후진해야됨
        back_y, back_x = cur_y - dy[robot_dir], cur_x - dx[robot_dir]
        if graph[back_y][back_x] == 1:  # 뒤로 가려고 봤더니 벽이야
            print(result)
            exit(0)
        else:  # 뒤로 갈 수 있어.
            cur_y, cur_x = back_y, back_x   # 후진.
