import math
import sys
input = sys.stdin.readline

n, m = map(int, input().split(':'))
num = math.gcd(n, m)
n /= num
m /= num
print(str(int(n)) + ':' + str(int(m)))