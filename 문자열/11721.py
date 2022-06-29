import sys
from collections import deque

input = sys.stdin.readline
data = input()

check=0
line=""
for char in data:
    if check == 10:
        print(line.rstrip())
        line=""
        check=0
    line += char
    check+=1

print(line.rstrip())