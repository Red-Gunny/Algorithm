import sys
input = sys.stdin.readline

data = list(map(int, input().rstrip()))


if len(data) == 1:
    print(0)
    if data[0] % 3 == 0:
        print("YES")
    else:
        print("NO")
    exit(0)

cnt = 1
while True:
    challenge = 0
    for num in data:
        challenge += num
    if challenge < 10:
        print(cnt)
        if challenge % 3 == 0:
            print("YES")
        else:
            print("NO")
        break
    cnt += 1
    data = [int(a) for a in str(challenge)]