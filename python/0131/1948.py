import sys
sys.stdin = open('input.txt')

T = int(input())

# 월 별 최대 일수
dic = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
case_list = []
for t in range(T):
    case = list(map(int, input().split()))
    print(f'#{t+1}', end=' ')
    mon = case[2] - case[0]

    # 두 날짜의 월이 같을 경우
    if mon == 0:
        day = case[3] - case[1] + 1
        print(day)

    # 두 날짜의 월이 다를 경우
    else:
        day = 0
        for n in range(case[0], case[2] + 1):
            day += dic[n]
        day = day - case[1] - (dic[case[2]] - case[3]) + 1
        print(day)