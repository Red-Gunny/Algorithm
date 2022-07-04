import sys

input = sys.stdin.readline

N = int(input())

number_list = []
sixes = 666
check = 0
while True:
    if '666' in str(sixes):
        number_list.append(sixes)
        check += 1
        if check == N:
            break
    sixes += 1
print(number_list[N-1])
