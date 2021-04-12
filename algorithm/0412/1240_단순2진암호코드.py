import sys
sys.stdin = open('1240.txt')

dic = {
    '0001101': '0',
    '0011001': '1',
    '0010011': '2',
    '0111101': '3',
    '0100011': '4',
    '0110001': '5',
    '0101111': '6',
    '0111011': '7',
    '0110111': '8',
    '0001011': '9',
}

T = int(input())
for t in range(1, T + 1):
    print('#{}'.format(t), end=' ')
    N, M = map(int, input().split())
    temp = [list(map(str, input())) for _ in range(N)]
    for row in temp:
        for i in range(len(row) - 1, -1, -1):
            if row[i] == '1':
                code = row[i - 55:i + 1]
                break

    secret = ''
    for i in range(0, len(code), 7):
        digit = ''
        for j in range(i, i + 7):
            digit += code[j]
        secret += dic[digit]
    
    odd = 0
    even = 0
    for i in range(len(secret)):
        if not i % 2:
            odd += int(secret[i])
        else:
            even += int(secret[i])
        verify = odd * 3 + even
        res = odd + even

    if not verify % 10:
        print(res)
    else:
        print(0)