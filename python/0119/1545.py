# 주어진 숫자부터 0까지 순서대로 찍어보세요

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T, -1, -1):
    print(t, end=' ')