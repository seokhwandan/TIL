import sys
sys.stdin = open('1486.txt')

def f(i, sumV):
    global minV

    if sumV >= B:
        minV = min(sumV, minV)
    
    if i == N:
        return
    else:
        f(i + 1, sumV + H[i])
        f(i + 1, sumV)
        


T = int(input())
for t in range(1, T + 1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort(reverse=True)
    minV = 10000 * 20
    f(0, 0)
    print('#{} {}'.format(t, minV - B))
