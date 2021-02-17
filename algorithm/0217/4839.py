import sys
sys.stdin = open('4839.txt')

def binary(page, p):
    start = 1
    cnt = 0
    while start <= page:
        m = int((start + page) / 2)
        if m == p:
            break
        elif m > p:
            page = m
            cnt += 1
        else:
            start = m
            cnt += 1
    return cnt

T = int(input())
for t in range(1, T + 1):
    print(f'#{t}', end=' ')
    P, Pa, Pb = map(int, input().split())
    # print(binary(P, Pa), binary(P, Pb))
    if binary(P, Pa) > binary(P, Pb):
        print('B')
    elif binary(P, Pa) < binary(P, Pb):
        print('A')
    else:
        print(0)
    