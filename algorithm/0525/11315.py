import sys
sys.stdin = open('11315.txt')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    stone = [list(map(str, input())) for i in range(N)]
    dic = {}
    res = ''
    for x in range(N):
        for y in range(N):
            if stone[x][y] == 'o':
                if x + 1 not in dic.keys():
                    dic[x + 1] = [y + 1]
                else:
                    dic[x + 1] += [y + 1]
            else:
                if x + 1 not in dic.keys():
                    dic[x + 1] = []
    # print(dic)
    for i in range(1, N + 1):
        if dic[i] == [1, 2, 3, 4, 5]:
            res = 'YES'
        elif i in dic[i] or 6-i in dic[i]:
    print(res)
