# 입력으로 1개의 정수 N 이 주어진다.
# 정수 N 의 약수를 오름차순으로 출력하는 프로그램을 작성하라.

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

for n in range(1, N + 1):
    if N % n == 0:
        print(n, end=' ')
