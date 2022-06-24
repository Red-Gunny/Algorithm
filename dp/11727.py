import sys
input = sys.stdin.readline
N = int(input())

table = [0]*(N+1)
if N == 1 :
    print(1)
    exit(0)

table[1] = 1
table[2] = 3

for i in range(3, N+1) :
    table[i] = table[i-1] + 2*table[i-2]

print(table[N]%10007)