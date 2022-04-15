n, m = map(int, input().split())

list_cost = []              # 과목 하나당 어떻게 되는가 추려내기위한

for i in range(n) :
    applied_cost = []               # 리스트 선언 (과목 당 신청인원정보)
    applied, limited = map(int, input().split())
    applied_cost = list(map(int, input().split()))
    # input(applied_cost)
    applied_cost.sort(reverse=True)       # 큰게 앞으로
    last_idx = len(applied_cost)
    if last_idx >= limited :      #   5명 4명제한일 때    list (3) 맞죠   /  4명 4명일 떄  lt
        list_cost.append(applied_cost[limited-1])
    else :
        list_cost.append(1)

list_cost.sort()        # 작은거부터해야 많이 담을거 아님

challenge = 0
cnt_subject = 0
for cost in list_cost :
    challenge += cost
    cnt_subject+=1
    if challenge > m :
        challenge -= cost
        cnt_subject -=1
        break

print(cnt_subject)