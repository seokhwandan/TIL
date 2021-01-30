import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1): 
    N = int(input())
    txt = ''
    for i in range(1, N + 1):
        Ci, Ki = input().split()
        Ki = int(Ki)
        # print(Ci, Ki)
        while True:
            if Ki < 1:
                break
            txt += Ci
            Ki -= 1
    print(f'#{t}')
    # print(txt)
    count = 1
    for j in txt:
        print(j, end='')
        if count % 10 == 0:
            print()
        count += 1
    print()