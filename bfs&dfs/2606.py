from collections import deque

n = int(input())    # 입력받아
connect = int(input())  # 연결 수
graph = [[] for i in range(n+1)]        # [ [], [], [].. , [] ]  처럼 생김 내부 요소는 connect의 수
visited = [False]*(n+1)                 # 컴퓨터수 + 1만큼 배열?

cnt = 0

for i in range(connect) :
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

def bfs(graph, v) :
    global cnt
    queue = deque([v])
    while queue :
        pop = queue.popleft()
        visited[pop] = True
        for i in graph[pop] :
            if visited[i] == False :
                visited[i] = True
                queue.append(i)
                cnt += 1

