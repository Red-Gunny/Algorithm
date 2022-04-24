from collections import deque

N = int(input())
region = []
maxNum=0
for i in range(N):
    region.append(list(map(int, input().split())))
    ### 문제파악 못하고 추가된 부분
    for j in range(N):
        if region[i][j] > maxNum:
            maxNum=region[i][j]

dx=[1,0,-1,0]
dy=[0,-1,0,1]


def bfs(graph, x, y, value) :
    myQ = deque()
    myQ.append((x,y))
    visited[y][x]=True
    while myQ:
        cx, cy = myQ.popleft()
        # if is_safe(cx, cy, region, N) :
        for i in range(4) :
            nx, ny = cx+dx[i], cy+dy[i]
            if 0<=nx<N and 0<=ny<N and not visited[ny][nx]:
                visited[ny][nx] = True
                if region[ny][nx] > value :
                    myQ.append((nx, ny))


result=0
for i in range(maxNum):
    visited = [[False] * N for i in range(N)]
    cnt=0

    for j in range(N):
        for k in range(N):
            if region[j][k] > i and not visited[j][k]:
                bfs(region, k, j, i)
                cnt+=1

    if result < cnt:
        result = cnt

print(result)