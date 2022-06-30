import sys

input = sys.stdin.readline

N = int(input())
p = list(map(int, input().split()))
p.insert(0,0)
record = [0]*(N+1)
record[1] = p[0]       # 1장만 산다고 했을 때 !
record[2] = max(record[1] + p[0], p[1])       # 2장 산다고 했을 때 최대값
for i in range(1, N+1):
    for j in range(1, i+1):
        record[i] = max(record[i], p[j] + record[i-j])
print(record[N])