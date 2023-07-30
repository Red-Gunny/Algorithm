import sys

input = sys.stdin.readline


N, M = map(int, input().split())
true_people = list(map(int, input().split()))
true_people = true_people[1:]

parent = [i for i in range(N+1)]
all_party = []


def get_parent(node):
    if node == parent[node]:
        return node
    return get_parent(parent[node])


def union_parent(node1, node2):
    pa1 = get_parent(node1)
    pa2 = get_parent(node2)
    if pa1 < pa2:
        parent[pa2] = pa1
    else:
        parent[pa1] = pa2


for _ in range(M):
    party = list(map(int, input().split()))
    all_party.append(party)
    member_cnt = party[0]
    for i in range(1, member_cnt):
        man1, man2 = party[i], party[i+1]
        union_parent(man1, man2)


parent_set = set()
for true_man in true_people:
    parent_set.add(get_parent(true_man))

answer = 0
for party in all_party:
    pa = get_parent(party[1])
    if pa not in parent_set:
        answer += 1
print(answer)





