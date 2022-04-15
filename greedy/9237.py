N = int(input())

tree = list(map(int, input().split()))    # 리스트로 입력받기

tree.sort(reverse=True)

i=1
list = []

for data in tree :
    list.append(data+i)
    i=i+1

before = list[0]
for data in list :
    if data > before :
        before = data

print(before + 1)