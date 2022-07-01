import sys
input = sys.stdin.readline

N, M = map(int, input().split())
data = [list(map(str, input().rstrip())) for _ in range(N)]

agtc = {'A': 0, 'G': 0, 'T': 0, 'C': 0}
result = ""
dist=0

for i in range(M):
    agtc['A'], agtc['G'], agtc['T'], agtc['C'] = 0, 0, 0, 0
    for j in range(N):
        agtc[data[j][i]] += 1
    cnt_list = list(agtc.values())
    cnt_list.sort(reverse=True)
    char = cnt_list[0]
    result_char = ''
    if agtc['A'] == char:
        result += 'A'
        result_char = 'A'
    elif agtc['C'] == char:
        result += 'C'
        result_char = 'C'
    elif agtc['G'] == char:
        result += 'G'
        result_char = 'G'
    else:
        result += 'T'
        result_char = 'T'
    for j in range(N):
        if data[j][i] != result_char:
            dist += 1
    cnt_list.clear()


print(result)
print(dist)