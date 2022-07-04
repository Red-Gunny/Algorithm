import sys
import math

input = sys.stdin.readline

N = int(input())
for _ in range(N):
    S = list(map(int, input().split()))
    n = S[0]
    result = 0
    for i in range(1, len(S)):
        for j in range(i+1, len(S)):
            GCD = math.gcd(S[i], S[j])
            result += GCD
    print(result)