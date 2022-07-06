import sys

input = sys.stdin.readline
N, M, x, y, K = map(int, input().split())

############# x, y에서 문제가 있었음 (이후에 내가 다룰 때 거꾸로 다룸) #############################################

###
top, bottom, front, back, left, right = 0, 0, 0, 0, 0, 0
####

def move_pos(num):
    global top, bottom, front, back, left, right
    global xPos, yPos
    if num == 1:    # 동
        bottom, right, top, left = right, top, left, bottom
        xPos += 1
    elif num == 2:  # 서
        bottom, left, top, right = left, top, right, bottom
        xPos -= 1
    elif num == 3:  # 북
        bottom, back, top, front = back, top, front, bottom
        yPos -= 1
    elif num == 4:  # 남
        bottom, front, top, back = front, top, back, bottom
        yPos += 1

def next_checking(num):
    next_xPos, next_yPos = xPos, yPos
    if num == 1:        # 동쪽
        next_xPos = xPos + 1
    elif num == 2:      # 서쪽
        next_xPos = xPos - 1
    elif num == 3:      # 북쪽
        next_yPos = yPos - 1
    elif num == 4:      # 남쪽
        next_yPos = yPos + 1
    if next_xPos < 0 or next_xPos >= M or next_yPos < 0 or next_yPos >= N:
        return False
    return True

graph = [list(map(int, input().split())) for _ in range(N)]
order = list(map(int, input().split()))

xPos, yPos = y, x
for i in order:
    if not next_checking(i):
        #print(yPos, xPos)
        continue
    move_pos(i)      # ㄹㅇ 이동
    if graph[yPos][xPos] == 0:
        graph[yPos][xPos] = bottom
    else:
        bottom = graph[yPos][xPos]
        graph[yPos][xPos] = 0
    print(top)
    '''
    if graph[yPos][xPos] != 0:      # 바닥에 뭔가가 적혀있음
        bottom = graph[yPos][xPos]      # 칸에 쓰여있는 수가 주사위 바닥면으로 복사되며
        graph[yPos][xPos] = 0           # 칸에있는 수는 0이된다
    elif graph[yPos][xPos] == 0:
        graph[yPos][xPos] = bottom      #주사위 바닥면에 쓰여있는 수가 칸에 복사됨'''

