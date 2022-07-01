import sys
input = sys.stdin.readline

data = input().rstrip()
data_list = []
for i in range(len(data)):
    data_list.append(data[i:])
data_list.sort()
for string in data_list:
    print(string)