import sys
sys.stdin = open('11753.txt')

T = int(input())
for t in range(1, T + 1):
    print('#{}'.format(t), end=' ')
    N = float(input())
    n = N * 2
    
    ans = ''
    while n != 1:
        if len(ans) > 13:
            break

        if n > 1:
            ans += '1'
            n = (n - 1) * 2
        if n < 1:
            ans += '0'
            n = n * 2
    if n == 1:
        ans += '1'
    
    if len(ans) < 13:
        print(ans)
    else:
        print('overflow')