# 1부터 주어진 숫자만큼 모두 더한 값을 출력하시오.
# 단, 주어질 숫자는 10000을 넘지 않는다.

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

s = 0
for t in range(T + 1):
    s += t
print(s)