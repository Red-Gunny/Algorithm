import sys

input = sys.stdin.readline

str = input().rstrip()
list_str = list(str)

set_str = set()

for i in range(len(list_str)):
    set_str.add(list_str[i])
    ch = list_str[i]
    for j in range(i+1, len(list_str)):
        ch += list_str[j]
        set_str.add(ch)

print(len(set_str))