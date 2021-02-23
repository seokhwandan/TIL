import sys
sys.stdin = open('4873.txt')

T = int(input())
for t in range(1, T + 1):
    word = input()
    lst = []
    cnt = 0
    for i in word:
        lst.append(i)
        if len(lst) >= 2 and lst[-2] == lst[-1]:
            lst = lst[:-2]
            cnt += 1
    print('#{} {}'.format(t, len(lst)))