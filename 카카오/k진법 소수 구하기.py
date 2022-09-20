import math

n = 110011
k = 10

def solution(n, k):
    answer = 0
    jinbuped = get_k_jibup(n, k)
    number_list = jinbuped.split('0')
    for number in number_list:
        if len(number) == 0:
            continue
        if int(number) < 2:
            continue
        if is_prime(int(number)):
            answer += 1
    return answer

def get_k_jibup(n, k):
    result = ""
    comp = n
    while comp > 0:
        tmp = comp % k
        comp = comp // k
        result += str(tmp)
    result = result[::-1]
    return result

def is_prime(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

print(solution(n, k))