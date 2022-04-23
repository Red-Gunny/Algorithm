M, N, K = map(int, input().split()) # Y좌표, X좌표, 직사각형 개수

graph = [[0]*N for i in range(M)]    # X길이 & Y길이
visited = [[False for j in range(N)] for i in range(M)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for i in range(K) :
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(y1, y2):
        for k in range(x1, x2):
            graph[j][k] = 1
            visited[j][k] = True

global cnt

def dfs3(x, y):
    global cnt
    cnt += 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if not visited[ny][nx]:
                visited[ny][nx] = True
                dfs3(nx, ny)

result=[]
cnt_island =0
for i in range(N):
    for j in range(M):
        if not visited[j][k]:
            cnt=0
            dfs3(k, j)
            cnt_island+=1
            result.append(cnt)

print(cnt_island)




