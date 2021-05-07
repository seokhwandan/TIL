import sys
sys.stdin = open('10912.txt')

T = int(input())
for t in range(1, T + 1):
    print(f'#{t}', end=' ')
    string = input()
    S = []
    res = ''
    for s in string:
        if s in S:
            S.remove(s)
        else:
            S.append(s)
    S.sort()
    if S == []:
        res = 'Good'
    else:
        res = ''.join(S)
    print(res)