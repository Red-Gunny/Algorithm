import sys

sys.setrecursionlimit(15000)

input = sys.stdin.readline

N = int(input())    # 수행해야할 작업
graph = []
v = [-1]*(10001)    # 각 작업마다 수행이 끝나는 시간을 나타냄

min_result = 0

for i in range(N):
    lst = list(map(int, input().split()))
    if lst[1] == 0: # 선행 작업이 없으면
        v[i+1] = lst[0] # 끝나는 시간을 기록
        min_result = max(min_result, lst[0])        # 정답을 구하기 위함.
    graph.append(lst)   # 그래프에 집어넣음

def recurs(job_num):
    if v[job_num] != -1:
        return v[job_num]
    result = 0       # 맥시멈을 계산하기 위함.
    for i in range(graph[job_num-1][1]):  # 선행 job들에 대하여
        result = max(result, recurs(graph[job_num-1][2+i]))   # 가장 많이 걸리는 시간을 구해냄.
    v[job_num] = result + graph[job_num-1][0]   # 해당 job번호의 끝나는 시간을 기록함.
    global min_result
    min_result = max(min_result, v[job_num])
    return v[job_num]

for i in range(N):
    recurs(i+1)

print(min_result)
