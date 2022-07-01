import sys
input = sys.stdin.readline

N = int(input())
members = []
db = {}

for _ in range(N):
    name, day, month, year = input().split()
    members.append((int(year), int(month), int(day)))
    db[year+month+day] = name       # 생일을 키값으로 이름을 저장

members.sort()
year, month, day = members[0]
ggondae = str(year)+str(month)+str(day)

members.sort(reverse=True)
year, month, day = members[0]
young = str(year)+str(month)+str(day)

print(db[young])
print(db[ggondae])

