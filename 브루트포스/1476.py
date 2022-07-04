import sys

input = sys.stdin.readline

E, S, M = map(int, input().split())

cnt_E, cnt_S, cnt_M = 1, 1, 1
year = 1
while True:
    if cnt_E == E and cnt_S == S and cnt_M == M:
        print(year)
        break
    cnt_E += 1
    cnt_S += 1
    cnt_M += 1
    year += 1
    if cnt_E > 15:
        cnt_E = 1
    if cnt_S > 28:
        cnt_S = 1
    if cnt_M > 19:
        cnt_M = 1


