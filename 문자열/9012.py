import sys
input = sys.stdin.readline

N = int(input())

data = [list(input().rstrip()) for _ in range(N)]

result = []
cond = False
stack = []
for string in data:
    cond = False
    for char in string:
        if char == '(':
            stack.append('(')
        elif len(stack) != 0 and char == ')':
            stack.pop()
        elif len(stack) == 0 and char == ')':
            result.append("NO")
            cond = True
            break
    if cond:
        continue
    if len(stack) == 0:
        result.append("YES")
    else :
        result.append("NO")
    stack.clear()

for ans in result:
    print(ans)