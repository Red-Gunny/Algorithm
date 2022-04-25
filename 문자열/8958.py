N = int(input())
for i in range(N):
    str = input()
    result=0
    score=0
    for j in str:
        if j == 'O':
            score += 1
            result += score
        else :
            score=0
    print(result)