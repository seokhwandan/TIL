import sys
sys.stdin = open('4865.txt')

T = int(input())

for t in range(1, T + 1):
    str1 = input()
    str2 = input()

    # # str1 각 문자에 카운트를 세기 위함
    # cnt = [0] * len(str1)

    # # str1의 길이만큼 순회
    # for i in range(len(str1)):
    #     # str1[i] 가 str2에 몇개 들어있는지 체크
    #     for j in range(len(str2)):
    #         if str1[i] == str2[j]:
    #             cnt[i] += 1

    # ans = 0
    # # 가장 큰 값 찾기
    # for i in range(len(cnt)):
    #     if ans < cnt[i]:
    #         ans = cnt[i]

    # print('#{} {}'.format(t, ans))

    # 키 = 문자, value = 카운트한 수
    my_dict = {}
    # str1의 문자를 가진 딕셔너리 생성
    for key in str1:
        my_dict[key] = 0
    for key in str2:
        if key in my_dict:
            my_dict[key] += 1
    ans = 0
    for i in my_dict.values():
        if ans < i:
            ans = i
    print('#{} {}'.format(t, ans))