str = input()

before = str[0]
cnt_zero = 0
cnt_one = 0

record=-1

for char in str :
    if before != char :
        if char == '1' :
            cnt_zero = cnt_zero + 1
            record = 1
        if char == '0' :
            cnt_one = cnt_one + 1
            record = 0
    before = char

if record == 1 :
    cnt_one = cnt_one+1
elif record == 0 :
    cnt_zero = cnt_zero+1

#print(cnt_zero)
#print(cnt_one)

if cnt_zero < cnt_one :
    print(cnt_zero)
else :
    print(cnt_one)