import sys
import itertools

input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

cnt_team = int(N/2)

def get_other_teams(member_list):
    member_set = set(member_list)
    mems = [i+1 for i in range(N)]
    whole_set = set(mems)
    return whole_set - member_set

def get_teams_stat(member_list):
    idxes = list(itertools.permutations(member_list, 2))
    sum = 0
    for i in idxes:
        sum += graph[i[0]-1][i[1]-1]
    return sum

whole_team = set()
for i in range(1, N+1):
    whole_team.add(i)
one_team = list(itertools.combinations(range(1, N+1), cnt_team))
result = int(1e9)
for members in one_team:
    other_team = get_other_teams(members)
    other_sum = get_teams_stat(other_team)
    were_sum = get_teams_stat(members)
    result = min(result, abs(other_sum - were_sum))

print(result)