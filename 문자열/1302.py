import sys

input = sys.stdin.readline

N = int(input())
db = {}
for_sort = []
for _ in range(N):
    sold_name = input().rstrip()
    if sold_name not in db:
        db[sold_name] = 1
    else:
        db[sold_name] += 1
sorted_db = sorted(db.items(), key=lambda item: (-item[1], item[0])) #, reverse=True
print(sorted_db[0][0])
