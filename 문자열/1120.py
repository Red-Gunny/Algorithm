import sys

input = sys.stdin.readline

A, B = map(list, input().rstrip().split())
#A = list(A.rstrip())
#B = list(B.rstrip())
iterate_cnt = len(B) - len(A) + 1   # 무조건 1이상.
optimal = 100
for i in range(iterate_cnt):
    diff_cnt = 0
    for j in range(len(A)):
        if A[j] != B[i+j]:    # j는 A문자 내에서 위치 / i는 몇번 왼쪽으로 움직였니
            #print(str(i) + "번째")
            #print(A[j] + "와" + B[i+j] + "가 달라")
            diff_cnt += 1
    if diff_cnt < optimal:  # 지금 있는 위치가 좋아~ (여기 조건문에 무조건 걸림)
        optimal = diff_cnt

print(optimal)