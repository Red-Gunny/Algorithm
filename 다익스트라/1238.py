import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

N, M, X = map(int, input().split())

graph = [[] for _ in range(N+1)]      # 여기 왜 M이 아니라 N

for _ in range(M) :
    start, end, time = map(int, input().split())
    graph[start].append((end, time))

# 다익스트라 코드
def dijkstra(start) :
    distance = [INF] * (N+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q :
        road_time, road_start = heapq.heappop(q)
        if distance[road_start] < road_time :
            continue
        for i in graph[road_start] :
            cost = road_time + i[1]     # 딱 한칸 더 까지의 비용
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

student_times = [[] for _ in range(N+1)]      # 세로로 N만큼 있는.. 근데 리스트 각각
each_student_times = []*(N+1)       # 그냥 리스트인데 크기가 N+1이라고 지정해놓은 것일뿐
comback_home=[]
for i in range(N+1) :   # 1부터 N까지
    if i == 0 :
        continue
    student_times[i] = dijkstra(i)      # 각 학생별 X 까지 가는데 걸리는 시간..
    if i == X :
        comback_home = student_times[i]
    each_student_times.append(student_times[i][X])          # 1번째에 4를 넣어라... ==  첫번째학생이 X까지 가는데 걸리는 시간이 4

student_result = [-1]*N       # 완전한 결과 담을 통
idx=0
biggest = 0
for data in each_student_times :        # [1]에 1이 X까지 가는데 걸리는 시간.
    student_result[idx] = data + comback_home[idx+1]
    if student_result[idx] > biggest :
        biggest = student_result[idx]
    idx += 1
print(biggest)