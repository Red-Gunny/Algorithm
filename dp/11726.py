import sys
input = sys.stdin.readline

N = int(input())
##test_list = [int(input()) for _ in range(N)]

d = [0]*1001

d[1] = 1
d[2] = 2


for i in range(3, 1001):
    d[i] = d[i-1] + d[i-2]

print(d[N]%10007)
