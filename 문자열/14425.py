import sys
input = sys.stdin.readline

N, M = map(int, input().split())
first = set()

for _ in range(N):
    data = input().rstrip()
    first.add(data)


result = 0
for _ in range(M):
    str = input().rstrip()
    if str in first:
        result += 1
print(result)