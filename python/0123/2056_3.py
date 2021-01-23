import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    date = input()
    y = date[0:4]
    m = date[4:6]
    d = date[6:8]

    if int(m) > 12 or int(m) < 1:
        print(f'#{t+1} -1')
    elif int(m) in {1, 3, 5, 7, 8, 10, 12} and int(d) > 31 or int(d) < 1:
        print(f'#{t+1} -1')
    elif int(m) in {4, 6, 9, 11} and int(d) > 30 or int(d) < 1:
        print(f'#{t+1} -1')
    elif int(m) == 2 and int(d) > 28 or int(d) < 1:
        print(f'#{t+1} -1')
    else:
        print(f'#{t+1} {y}/{m}/{d}')