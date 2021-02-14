import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(1, T + 1):
    print(f'#{i}', end=' ')
    txt = input().split()
    for j in txt:
        if j == j[::-1]:
            print(1)
        else:
            print(0)
