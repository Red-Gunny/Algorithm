import sys
input = sys.stdin.readline

string = input().rstrip()

result = 0
data = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'dz=', 'z=']

for char in data:
    string = string.replace(char, '*')
print(len(string))
