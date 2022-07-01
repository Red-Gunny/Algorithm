import sys
input = sys.stdin.readline

N = int(input())
result = 0

for i in range(N):
    string = input()  # 입력 문자열
    checker = dict()  # 딕셔너리 (키&값)
    before = string[0]  # 문자열의 첫번째 문자
    for char in string:
        if char not in checker:  # 키 중에 없으면 (이번이 처음보는 문자)
            checker[char] = 1
        else:  # 이미 들어간적이 있으면
            if before != char:  # 씨발 이전에 등장했는데 떨어져있어?
                result += 1  # 그룹단어 아닌거 추가여
                break
        before = char  # 기록~

print(N-result)