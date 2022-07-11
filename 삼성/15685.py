import sys
from collections import deque

input = sys.stdin.readline

def turn_right(start, before, after):
    if before[0] == after[0]:
        if before[1] + 1 == after[1]:       # x가 1만큼 증가함
            return start[0] + 1, start[1]       # 그러면 y가 1만큼 증가
        elif before[1] - 1 == after[1]:     # x가 1만큼 감소함
            return start[0] - 1, start[1]       # 그러면 y가 1만큼 감소함
    else:
        if before[0] + 1 == after[0]:       # y가 1만큼 증가했음
            return start[0], start[1] - 1       # 그러면 x가 1만큼 감소함
        elif before[0] - 1 == after[0]:     # y가 1만큼 감소했음
            return start[0], start[1] + 1       # 그러면 x가 1만큼 증가함

def trace_and_record(line_q, visited):
    idx = len(line_q) - 1
    tmp_q = list(line_q).copy()
    s_y, s_x = tmp_q[idx][0], tmp_q[idx][1]
    for i in range(len(tmp_q)-1, 0, -1):
        n_y, n_x = turn_right((s_y, s_x), tmp_q[i], tmp_q[i-1])
        line_q.append((n_y, n_x))
        visited[n_y][n_x] = 1
        s_y, s_x = n_y, n_x
    return line_q

K = int(input())    # 드래곤 커브 개수
visited = [[0] * 101 for _ in range(101)]
for _ in range(K):
    x, y, d, g = map(int, input().split())
    line_q = deque()
    line_q.append((y, x))
    visited[y][x] = 1
    if d == 0:  # 값 똑바로 증가했는지 실수 주의
        line_q.append((y, x+1))
        visited[y][x+1] = 1
    elif d == 1:
        line_q.append((y-1, x))
        visited[y-1][x] = 1
    elif d == 2:
        line_q.append((y, x-1))
        visited[y][x-1] = 1
    elif d == 3:
        line_q.append((y+1, x))
        visited[y+1][x] = 1

    for _ in range(g):
        line_q = trace_and_record(line_q, visited)
    line_q.clear()

result = 0
for i in range(100):        # 실제 0부터 99 까지
    for j in range(100):    # 실제 0부터 99 까지
        if visited[i][j] == 1 and visited[i+1][j] == 1 and visited[i][j+1] == 1 and visited[i+1][j+1] == 1:
            result += 1

print(result)