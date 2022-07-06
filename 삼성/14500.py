import sys

input = sys.stdin.readline
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 하나의 좌표 기준으로 합을 반환함.
def get_blue_sum_max(yPos, xPos):
    # 가로
    garo = 0
    for i in range(4):
        if not 0 <= yPos < N or not 0 <= xPos+3 < M:  # 그래프 범위 밖
            garo = 0
            break
        garo += graph[yPos][xPos+i]  # 그래프 이내면 더함.
    # 세로
    sero = 0
    for i in range(4):
        if not 0 <= yPos+3 < N or not 0 <= xPos < M:
            sero = 0
            break
        sero += graph[yPos+i][xPos]
    return max(garo, sero)

# 애초에 이게 맥스임 다른 조건 x
def get_yello_sum_max(yPos, xPos):
    # 대칭해도 모두 동일함.
    sum = 0
    if 0 <= yPos + 1 < N and 0 <= xPos + 1 < M:
        for i in range(2):
            for j in range(2):
                sum += graph[yPos+i][xPos+j]
    return sum

def get_green_sum_max(yPos, xPos):
    case1, case2, case3, case4 = 0, 0, 0, 0
    # case 1
    if yPos+2 < N and xPos+1 < M:
        case1 = graph[yPos][xPos] + graph[yPos+1][xPos] + graph[yPos+1][xPos+1] + graph[yPos+2][xPos+1]
    if yPos+2 < N and xPos-1 >= 0:
        case2 = graph[yPos][xPos] + graph[yPos+1][xPos] + graph[yPos+1][xPos-1] + graph[yPos+2][xPos-1]
    if yPos-1 >= 0 and xPos+2 < M:
        case3 = graph[yPos][xPos] + graph[yPos][xPos+1] + graph[yPos-1][xPos+1] + graph[yPos-1][xPos+2]
    if yPos+1 < N and xPos+2 < M:
        case4 = graph[yPos][xPos] + graph[yPos][xPos+1] + graph[yPos+1][xPos+1] + graph[yPos+1][xPos+2]
    return max(case1, case2, case3, case4)

'''
현재 좌표에서 오렌지와 핑크 중 가장 맥스 값을 반환함.
'''
def get_orange_or_pink_max(yPos, xPos):
    # 막대기 (사이즈 3짜리)
    three_garo, three_sero = get_three_bar(yPos, xPos)

    # 가로로에 대해서 위아래 가능한 케이스를 따짐
    garo_max = 0
    if three_garo != 0:
        if 0 <= yPos - 1:   # 가로축 기준 위에 한칸이 여유
            for i in range(3):      # 가로축이 0이 아니란거는 xPos에 대해서는 예외처리 할 필요가 없음. (직사각형이니까!)
                garo_max = max(graph[yPos - 1][xPos + i] + three_garo, garo_max)
        if yPos + 1 < N:    # 가로축 기준 밑에 한칸이 여유
            for i in range(3):
                garo_max = max(graph[yPos + 1][xPos + i] + three_garo, garo_max)

    # 세로로에 대해서 위아래 가능한 케이스를 따짐
    sero_max = 0
    if three_sero != 0:
        if 0 <= xPos - 1:
            for i in range(3):
                sero_max = max(graph[yPos+i][xPos-1] + three_sero, sero_max)
        if xPos + 1 < M:
            for i in range(3):
                sero_max = max(graph[yPos+i][xPos+1] + three_sero, sero_max)
    return max(garo_max, sero_max)

''' [주의] 가로 세로 순'''
''' 0인 경우 처리할 때 주의 필 '''
def get_three_bar(yPos, xPos):
    # 가로 막대기 (3짜리)
    garo_mid = 0
    if xPos+2 < M:
        for i in range(3):
            garo_mid += graph[yPos][xPos + i]

    # 세로 막대기 (3짜리)
    sero_mid = 0
    if yPos+2 < N:
        for i in range(3):
            sero_mid += graph[yPos + i][xPos]

    return garo_mid, sero_mid

result = 0
for i in range(N):
    for j in range(M):
        result = max(
            result,
            get_blue_sum_max(i, j),
            get_yello_sum_max(i, j),
            get_green_sum_max(i, j),
            get_orange_or_pink_max(i, j)
        )
print(result)