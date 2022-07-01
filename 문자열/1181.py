import sys
input = sys.stdin.readline

N = int(input())

len_words = {}
words_list = []

for _ in range(N):
    str = input().rstrip()
    if str in len_words:            # dictionary 이거 해시임
        continue                    # 이미 함 했으니까 무시무시해
    len_words[str] = len(str)
    words_list.append((len(str), str))

words_list.sort()
for len, str in words_list:
    print(str)

