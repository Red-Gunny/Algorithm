str = input()

result ={}

for data in str :
    if data not in result :        # 없음
        result[data] = 1
    else :                         # 있음
        result.update({ data : result[data]+1 })

oddcnt=0
evencnt=0

odd_char = ''

for key, val in result.items() :
    if val % 2 == 1:
        oddcnt+=1
        odd_char = val
    else :
        evencnt+=1

sorted(result.keys())

if oddcnt > 1 :
    print("I'm Sorry Hansoo")
elif oddcnt == 1 :

else :


str=""

