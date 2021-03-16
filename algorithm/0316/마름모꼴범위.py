# 10x10 범위에서 어느 한 점과 범위가 주어졌을 때
# 마름모꼴 범위를 구하는 방법

lst = [[0] * 10 for _ in range(10)]
n = 3 # 범위
r, c = 4, 5 # 마름모의 중앙 위치

for i in range(10):
    for j in range(10):
        if abs(r - i) + abs(c - j) <= n:
            lst[i][j] = 1
print(lst)