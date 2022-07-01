import sys
input = sys.stdin.readline

N, M = map(int, input().split())
db = {}
result = []
for i in range(N):
    name = input().rstrip()
    db[name] = i

for i in range(M):
    name = input().rstrip()
    if db.get(name) is not None:
        result.append(name)
result.sort()
print(len(result))
for answer in result:
    print(answer)