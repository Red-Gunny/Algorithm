import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
convey = deque(map(int, input().split()))   # 가중치값을 담는다.
robot_arr = [0]*(N+N)           #

robot_locate = {}      # {로봇ID : 로봇위치}
id_generator = 1

zero_cnt = 0            # 0의 개수
remove_ready = deque()      #

stage = 0
while True:
    stage += 1
    # 1 단계
    convey.rotate()  # 1. 로봇과 한 칸 회전
    if robot_locate:  # 로봇이 올라가 있으면
        for id, locate in robot_locate.items():  # 로봇들의 id / 위치
            robot_locate[id] = locate + 1  # 컨베이어에 의한 이동
            if locate + 1 == N - 1:         # 다 간 case
                robot_locate[id] = -1
                remove_ready.append(id)

    # 다 끝난 로봇이 있으면 탈출한다.
    while remove_ready:
        id = remove_ready.popleft()
        del robot_locate[id]

    # 2단계 - 로봇이 자체적으로 이동한다.
    if robot_locate:
        for id, locate in robot_locate.items():
            if id - 1 in robot_locate.keys():
                if robot_locate[id - 1] == locate + 1:  # 먼저 간놈의 위치가 내가 가려는곳에 이미 로봇이 있음 (못감 ㅠㅠ)
                    continue
            if convey[locate + 1] == 0:  # 내 앞 내구도가 0임 (못감 ㅠㅠ)
                continue
            if convey[locate + 1] >= 1:  # 나를 막는 애가 없고 내구도가 1이상이라 쌉가능 ㅎㅎ
                if convey[locate + 1] == 1:
                    zero_cnt += 1
                    if zero_cnt == K:
                        print(stage)
                        exit(0)
                robot_locate[id] = locate + 1  # 위치 이동
                convey[locate + 1] -= 1  # 컨베이 내구도 감소
            if locate + 1 == N - 1:  # 끝에 도달했다
                robot_locate[id] = -1
                remove_ready.append(id)

    # 다 끝난 로봇이 있으면 탈출한다.
    while remove_ready:
        id = remove_ready.popleft()
        del robot_locate[id]

    # 3단계 - 로봇을 새로 올린다.
    if convey[0] != 0:
        if convey[0] == 1:
            zero_cnt += 1
            if zero_cnt == K:
                print(stage)
                exit(0)
        robot_locate[id_generator] = 0  # 로봇 딕셔너리에 삽입
        id_generator += 1
        convey[0] -= 1

