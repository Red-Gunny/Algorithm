from collections import deque

N, M = map(int, input().split())
board = []
for _ in range(N) :
    board.append(list(map(int, input())))

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

visited = [[0]*M for _ in range(N)]

deq = deque([(0,0)])

visited[0][0] = 1


while deq :
    x, y = deq.popleft()

    if x == N-1 and y == M-1 :
        print(visited[x][y])

    for i in range(4) :
        nx, ny = x + dx[i], y+dy[i]

        if 0 <= nx < N and 0 <= ny < M :
            if visited[nx][ny] == 0 and board[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                deq.append((nx,ny))