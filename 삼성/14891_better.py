import sys

input = sys.stdin.readline

topnis = []
topnis.append([])  # 인덱스 1부터 시작해도 됨
for _ in range(4):
    topnis.append(list(map(int, input().rstrip())))
N = int(input())
rotate_list = [tuple(map(int, input().split())) for _ in range(N)]  # 회전 정보
# 입력 파싱 완료

def find_rotate_topni(topni_idx, topni_dir):
    global recurse_cnt
    if recurse_cnt >= 4:  # 재귀 탈출 조건
        return
    if topni_idx == 1:  # 1번 톱니바퀴 회전
        if topnis[topni_idx][2] != topnis[topni_idx + 1][6] and not visited[topni_idx + 1]:  # 오른쪽이랑 회전하는거면
            rotate_q.append((topni_idx + 1, topni_dir * (-1)))  # 톱니 번호 / 방향 정보
            visited[topni_idx] = True
            recurse_cnt += 1
            find_rotate_topni(topni_idx + 1, topni_dir * (-1))
    elif topni_idx == 2 or topni_idx == 3:  # 2번 톱니바퀴
        if topnis[topni_idx - 1][2] != topnis[topni_idx][6] and not visited[topni_idx - 1]:  # 왼쪽이랑 회전하는데 아직 방문된게 아니면
            rotate_q.append((topni_idx - 1, topni_dir * (-1)))
            visited[topni_idx] = True
            recurse_cnt += 1
            find_rotate_topni(topni_idx - 1, topni_dir * (-1))
        if topnis[topni_idx][2] != topnis[topni_idx + 1][6] and not visited[topni_idx + 1]:  # 오른쪽이랑 회전하는 거면
            rotate_q.append((topni_idx + 1, topni_dir * (-1)))
            visited[topni_idx] = True
            recurse_cnt += 1
            find_rotate_topni(topni_idx + 1, topni_dir * (-1))
    elif topni_idx == 4:
        if topnis[topni_idx - 1][2] != topnis[topni_idx][6] and not visited[topni_idx - 1]:  # 왼쪽이랑 회전해야되며는
            rotate_q.append((topni_idx - 1, topni_dir * (-1)))
            visited[topni_idx] = True
            recurse_cnt += 1
            find_rotate_topni(topni_idx - 1, topni_dir * (-1))

rotate_q = []
visited = [False] * 5
recurse_cnt = 0

for idx, direction in rotate_list:
    rotate_q.append((idx, direction))
    find_rotate_topni(idx, direction)
    for i, d in rotate_q:
        if d == 1:
            topnis[i].insert(0, topnis[i].pop())
        elif d == -1:
            topnis[i].append(topnis[i].pop(0))
    rotate_q.clear()
    visited = [False] * 5
    recurse_cnt = 0

result = 0
for i in range(1, 5):
    if topnis[i][0] == 1:
        mid = 1
        for j in range(i-1):
            mid *= 2
        result += mid
print(result)
