import sys
import copy
import itertools
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())    # N은 세로  / M은 가로
graph = [list(map(int, input().split())) for _ in range(N)]

test_graph = copy.deepcopy(graph)

result = 0
default_one = 0
default_two = 0

two_list = []
zero_list = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            zero_list.append((i, j))
        elif graph[i][j] == 1:
            default_one += 1
        elif graph[i][j] == 2:
            two_list.append((i, j))
            default_two += 1

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def bfs(yPos, xPos, board):
    cnt_two = 0
    visited = [[0] * M for _ in range(N)]
    q = deque()
    q.append((yPos, xPos))
    visited[yPos][xPos] = 1
    while q:
        cur_y, cur_x = q.popleft()
        for i in range(4):
            next_y, next_x = cur_y + dy[i], cur_x + dx[i]
            if 0 <= next_y < N and 0 <= next_x < M and visited[next_y][next_x] == 0:     # 그다음 좌표가 범위 이내면
                if board[next_y][next_x] == 0:
                    board[next_y][next_x] = 2
                    cnt_two += 1
                    visited[next_y][next_x] = 1
                    q.append((next_y, next_x))      # 큐 삽입.
    return cnt_two

comb_list = list(itertools.combinations(zero_list, 3))

result = 0
for first, second, third in comb_list:
    after_two = 0
    test_graph[first[0]][first[1]], test_graph[second[0]][second[1]], test_graph[third[0]][third[1]] = 1, 1, 1
    for two_y, two_x in two_list:
        after_two += bfs(two_y, two_x, test_graph)
    safe_zone = (N*M) - (default_one + default_two + after_two + 3)
    result = max(result, safe_zone)
    test_graph = copy.deepcopy(graph)
print(result)
