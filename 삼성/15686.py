import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())    # N은 정사각형 크기 / M은 치킨집 수
graph = [list(map(int, input().split())) for _ in range(N)]

home_list = []
chickens = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:    # 집 나올 때
            home_list.append((i, j))    # y, x 순
        elif graph[i][j] == 2:  # 치킨집 따리
            chickens.append((i, j))

survived_chickens = list(combinations(chickens, M))     # 살아남은 치킨 집 조합

def get_chicken_dist(home, chicken):    # 집 1개 ~ 치킨집 1개
    return abs(home[0] - chicken[0]) + abs(home[1] - chicken[1])

result = int(1e9)
for combinations in survived_chickens:      # M개 조합에 대하여
    city_dist = 0
    for home in home_list:      # 모든 집들에 대하여
        one_dist = int(1e9)
        for chicken in combinations:    # 치킨집 M개에 대하여
            one_dist = min(one_dist, get_chicken_dist(home, chicken))   # 거리를 구해나감
        city_dist += one_dist
    result = min(result, city_dist)

print(result)