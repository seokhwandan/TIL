import sys
sys.stdin = open('5432.txt')

T = int(input())
for t in range(1, T + 1):
    pipe = input()
    # ans = 0
    # cnt = 0
    # for i in range(len(pipe)):
    #     if pipe[i] == '(':
    #         cnt += 1
    #     else:
    #         cnt -= 1
    #         if pipe[i - 1] == '(':
    #             ans += cnt
    #         else:
    #             ans += 1
    # print('#{} {}'.format(t, ans))

    s = []
    ans = 0
    for i in range(len(pipe)):
        # 열린괄호라면 s 리스트에 넣어놓기
        if pipe[i] == '(':
            s.append('(')
        else:
            # 무조건 꺼내기
            s.pop()
            # 레이저
            if pipe[i - 1] == '(':
                ans += len(s)
            else:
                ans += 1
    print('#{} {}'.format(t, ans))