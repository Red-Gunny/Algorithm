import sys
from collections import deque

input = sys.stdin.readline

N = int(input())    # 보드 크기
K = int(input())    # 사과 개수
apples = [tuple(map(int, input().split())) for _ in range(K)]  # 사과 좌표 ### 1부터 시작함

''' 1부터 시작함에 주의할것 !!!'''

direct_cnt = int(input())
direct_list = []
for _ in range(direct_cnt):
    X, C = input().split()    # 방향전환 시간 / 방향
    direct_list.append((int(X), C))
'''파싱 완료'''

snake = []  # 뱀의 몸통 정보를 담음
head_y, head_x = 0, 0   # 뱀의 현재 대가리 주소
dy = [0, 1, 0, -1]  # 처음(오른쪽) / 밑 / 왼쪽 / 위  => D되면 ++ / L되면 --
dx = [1, 0, -1, 0]  # 오른쪽 / 밑 / 왼쪽 / 위      => D되면 ++ / L되면 --
cur_direct = 0      # dy dx를 조정함 (인덱스)

q_snake = deque()   # 뱀 몸통 정보 담을거임
q_snake.append((head_y, head_x))  # yPos, xPos 순 초기값
sec = 0 # 시간
while True:
    sec += 1 # 시간 증가
    next_y, next_x = head_y + dy[cur_direct], head_x + dx[cur_direct]   # 움직여 봄
    if not 0 <= next_y < N or not 0 <= next_x < N:  # 벽에 부딪혔다.
        print(sec)  # 시간 출력
        exit(0)     # 게임 종료
    if (next_y, next_x) in q_snake:   # 내 몸에 닿았나?
        print(sec)
        exit(0)
    if (next_y+1, next_x+1) in apples:  # 사과가 있네.
        q_snake.append((next_y, next_x))
        apples.remove((next_y+1, next_x+1))     # 사과 제거
    else:                               # 사과가 없네
        q_snake.popleft()
        q_snake.append((next_y, next_x))
    for num, ch in direct_list:     # 회전할 시간인가? (1 노상관)
        if num == sec:
            if ch == 'D':               # 오른쪽 회전이니까 ++
                cur_direct += 1
                cur_direct %= 4
            elif ch == 'L':             # 왼쪽 회전이니까 --
                cur_direct -= 1
                if cur_direct == -5 :
                    cur_direct = -1
    head_y, head_x = next_y, next_x     # 이제 다음거 기준되게 움직임
