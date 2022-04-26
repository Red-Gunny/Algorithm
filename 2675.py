T = int(input())

for _ in range(T):
    R,S = input().split()
    R = int(R)

    for character in S:
        for _ in range(R):
            print(character, end='')

    print("")