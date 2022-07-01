import sys
input = sys.stdin.readline

data = input().rstrip()

for i in range(len(data)):
    if data[i] == 'U':
        for j in range(i, len(data)):
            if data[j] == 'P':
                first_str = data[i+1:j]
                second_str = data[j+1:len(data)]
                if 'C' in first_str and 'C' in second_str:
                    print("I love UCPC")
                    exit(0)
print("I hate UCPC")
