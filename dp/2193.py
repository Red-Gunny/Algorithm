import sys
input = sys.stdin.readline
N = int(input())

if N == 1:
    print(1)
    exit(0)
elif N==2 :
    print(1)
    exit(0)

a_list = [-1]*(N+1)     # 0 카운팅 스타
b_list = [-1]*(N+1)     # 1 카운팅 스타

a_list[1] = 0
a_list[2] = 1

b_list[1] = 1
b_list[2] = 0

for i in range(3, N+1):
    a_list[i] = a_list[i-1]+b_list[i-1]
    b_list[i] = a_list[i-1]
print(a_list[N] + b_list[N])
