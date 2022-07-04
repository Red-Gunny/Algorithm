import sys

input = sys.stdin.readline

result = [i+1 for i in range(10000)]

for i in range(1, 10000):
    str_i = str(i)
    list_i = list(str_i)
    mid_sum = 0
    for digit in list_i:
        mid_sum += int(digit)
    idx = mid_sum + i - 1
    if idx < 10000:
        result[mid_sum+i-1] = 0

for i in result:
    if i != 0:
        print(i)