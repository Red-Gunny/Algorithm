import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

N, E = map(int, input().split())

adj_list = [[] for _ in range(N+1)]
distance1 = [INF]*(N+1)

for i in range(E):
    a, b, c = map(int, input().split())
    adj_list[a].append((b,c))
    adj_list[b].append((a,c))

must_a, must_b = map(int, input().split())

# parsing 완료
def dikstra(start, distance):
    q=[]
    heapq.heappush(q, (0, start))
    distance[start]=0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now] :
            continue
        for i in adj_list[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

distance1 = dikstra(1, distance1)

distance2 = [INF] * (N+1)
distance2 = dikstra(must_a, distance2)

distance3 = [INF] * (N+1)
distance3 = dikstra(must_b, distance3)

v1_path = distance1[must_a] + distance2[must_b] + distance3[N]       # start -> must_a -> must_b -> end
v2_path = distance1[must_b] + distance3[must_a] + distance2[N]       # start -> must_b -> must_a -> end

result = min(v1_path, v2_path)
if result < INF :
    print(result)
else :
    print(-1)



'''
# 비용 기록 완료 (1단계)
cost_a = distance1[must_a]
cost_b = distance1[must_b]


result_a = 0
result_b = 0




goAhead = False
cost_mid=0

def cost_a_is_small() :
    cost_mid = 0
    goAhead = False
    for data in adj_list[must_a]:
        if data[0] == must_b :
            cost_mid = data[1]          # 중간값 체킹 부분.
            goAhead=True
            break
    if not goAhead :
        print(str(-1))
        exit(0)
    ### 중간값 완료
    dikstra(must_b, distance2)
    cost_end_a = distance2[N]
    return cost_a + cost_mid + cost_end_a

def cost_b_is_small() :
    cost_mid = 0
    goAhead = False
    for data in adj_list[must_a]:
        if data[0] == must_b :
            cost_mid = data[1]          # 중간값 체킹 부분.
            goAhead=True
            break
    if not goAhead :
        print(str(-1))
        exit(0)
    ### 중간값 완료
    dikstra(must_b, distance2)
    cost_end_a = distance2[N]
    return cost_a + cost_mid + cost_end_a

result_A = cost_a_is_small()
result_B = cost_b_is_small()

if result_A > result_B :
    print(result_A)
else :
    print(result_B)'''