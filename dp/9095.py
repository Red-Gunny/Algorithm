import sys
input = sys.stdin.readline

N = int(input())
test_list = [int(input()) for _ in range(N)]

d = [0]*12

d[1] = 1
d[2] = 2
d[3] = 4
d[4] = 7

for i in range(5, 12):
    d[i] = d[i-1] + d[i-2] + d[i-3]

for idx in test_list :
    print(d[idx])
