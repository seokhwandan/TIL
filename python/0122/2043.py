# 서랍의 비밀번호가 생각이 나지 않는다.
# 비밀번호 P는 000부터 999까지 번호 중의 하나이다.
# 주어지는 번호 K부터 1씩 증가하며 비밀번호를 확인해 볼 생각이다.
# 예를 들어 비밀번호 P가 123 이고 주어지는 번호 K가 100 일 때, 100부터 123까지 24번 확인하여 비밀번호를 맞출 수 있다.
# P와 K가 주어지면 K부터 시작하여 몇 번 만에 P를 맞출 수 있는지 알아보자.

import sys
sys.stdin = open('input.txt', 'r')

P, K = list(map(int, input().split()))

count = 0
for n in range(K, P + 1):
    count += 1

print(count)