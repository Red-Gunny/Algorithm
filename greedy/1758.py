N = int(input())

list = []
for i in range(N) :
    num = int(input())
    list.append(num)

# print(list)

list.sort(reverse=True)

i=1
result = 0
for data in list :
    tmp = data - (i-1)
    if tmp > 0 :
        result += data - (i-1)
    i+=1

print(result)