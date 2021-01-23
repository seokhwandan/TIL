# 연월일 순으로 구성된 8자리의 날짜가 입력으로 주어진다.
# 해당 날짜의 유효성을 판단한 후, 날짜가 유효하다면
# [그림1] 과 같이 ”YYYY/MM/DD”형식으로 출력하고,
# 날짜가 유효하지 않을 경우, -1 을 출력하는 프로그램을 작성하라.
# 연월일로 구성된 입력에서 월은 1~12 사이 값을 가져야 하며
# 일은 [표1] 과 같이, 1일 ~ 각각의 달에 해당하는 날짜까지의 값을 가질 수 있다.
# ※ 2월의 경우, 28일인 경우만 고려한다. (윤년은 고려하지 않는다.)

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(T):
    date = input()

    y = date[0:4]
    m = date[4:6]
    d = date[6:8]

    if int(m) in (1, 3, 5, 7, 8, 10, 12):
        if int(d) < 32:
            print(f'#{t+1} {y}/{m}/{d}')
    elif int(m) in (4, 6, 9, 11):
        if int(d) < 31:
            print(f'#{t+1} {y}/{m}/{d}')
    elif int(m) == 2:
        if int(d) < 29:
            print(f'#{t+1} {y}/{m}/{d}')
        else:
            print(f'#{t+1} -1')
    else:
        print(f'#{t + 1} -1')
'''
    y = int(f'{date[0]}{date[1]}{date[2]}{date[3]}')
    m = int(f'{date[4]}{date[5]}')
    d = int(f'{date[6]}{date[7]}')

    str_y = f'{date[0]}{date[1]}{date[2]}{date[3]}'
    str_m = f'{date[4]}{date[5]}'
    str_d = f'{date[6]}{date[7]}'

    if m == 0:
        print(f'#{t + 1} -1')

    if 1 <= m <= 7:
        if m % 2 != 0:
            if d == 0:
                print(f'#{t+1} -1')
            elif d > 31:
                print(f'#{t+1} -1')
            else:
                print(f'#{t+1} {str_y}/{str_m}/{str_d}')


    if m == 2:
        if d == 0:
            print(f'#{t + 1} -1')
        elif d > 28:
            print(f'#{t + 1} -1')
        else:
            print(f'#{t + 1} {str_y}/{str_m}/{str_d}')

    if 2 < m <= 6:
        if m % 2 == 0:
            if d == 0:
                print(f'#{t+1} -1')
            elif d > 30:
                print(f'#{t+1} -1')
            else:
                print(f'#{t+1} {str_y}/{str_m}/{str_d}')

    if 8 <= m <= 12:
        if m % 2 == 0:
            if d == 0:
                print(f'#{t+1} -1')
            elif d > 31:
                print(f'#{t+1} -1')
            else:
                print(f'#{t+1} {str_y}/{str_m}/{str_d}')

        if m % 2 != 0:
            if d == 0:
                print(f'#{t+1} -1')
            elif d > 30:
                print(f'#{t+1} -1')
            else:
                print(f'#{t+1} {str_y}/{str_m}/{str_d}')
'''