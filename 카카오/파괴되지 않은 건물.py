import math
import copy
from itertools import combinations

board = [[1,2,3],[4,5,6],[7,8,9]]
skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]


def solution(board, skill):
    answer = 0
    tmp_board = copy.deepcopy(board)
    for line in skill:
        tmp_board = do_game(line, copy.deepcopy(tmp_board))
    for line in tmp_board:
        for data in line:
            if data > 0:
                answer += 1
    return answer

def do_game(info, board):
    type, r1, c1, r2, c2, degree = info
    for i in range(r1, r2+1):    # y좌표
        for j in range(c1, c2+1):   # x좌표
            if type == 1:
                board[i][j] -= degree
            elif type == 2:
                board[i][j] += degree
    return board



print(solution(board, skill))