N = int(input())

a_list = [0]*(N+1)
b_list = [0]*(N+1)

a_list[0] = 1
b_list[0] = 0

for i in range(1, N+1):
    a_list[i] = b_list[i-1]
    b_list[i] = a_list[i-1] + b_list[i-1]

print(a_list[N], end=' ')
print(b_list[N])