import sys

input = sys.stdin.readline

r, c, k = map(int, input().split())

A = []
for _ in range(3):
    A.append(list(map(int, input().split())))

row_size, col_size = 3, 3

def process_r(A):
    max_len = 0
    result = []
    # 가로로 조사함
    for line in A:
        num_dic = {}
        for num in line:
            if num == 0:
                continue
            if num not in num_dic:
                num_dic[num] = 1
            else:
                num_dic[num] += 1
        rslt_arr = sorted(num_dic.items(), key=lambda x: (x[1], x[0]))  # 정렬 수행

        # 다시 담기
        mid_result = []
        for value in rslt_arr:
            for v in value:
                mid_result.append(v)
        max_len = max(max_len, len(mid_result))         # 최대 길이 추출
        result.append(mid_result)

    for i in range(len(result)):
        if len(result[i]) < max_len:
            for _ in range(max_len - len(result[i])):
                result[i].append(0)                     # 0으로 넣기

    return result, max_len


def rotate_90(col_size, row_size, before):
    rotated = [[0]*col_size for _ in range(row_size)]
    for i in range(len(rotated)):
        for j in range(len(rotated[0])):
            rotated[i][j] = before[col_size-1-j][i]
    return rotated



def to_right(before):
    result_arr = [[0]*len(before[0]) for _ in range(len(before))]
    for i in range(len(before)):
        for j in range(len(before[0])):
            result_arr[j][i] = before[i][j]
    return result_arr


for i in range(101):
    print("row_size & col_size")
    print(row_size, col_size)
    input()
    if col_size >= row_size:
        A, row_size = process_r(A)                  #
        if A[r][c] == k:    # 문제 조건 검증
            print(i)
            exit(0)
    else:
        A = rotate_90(col_size, row_size, A)
        print("rotata 90")
        print(A)
        input()
        A, col_size = process_r(A)
        print("process _ A")
        print(A)
        input()
        A = to_right(A)
        print("rotate anti 90")
        print(A)
        input()
        if A[r][c] == k:
            print(i)
            exit(0)
    print(A)
    input()

print(-1)
    




