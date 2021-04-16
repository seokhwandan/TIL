import sys
sys.stdin = open('4366.txt')

def bi_cases(s):
    i = 0
    arr = []
    while i < len(s):
        if s[i] == '1':
            arr.append(int(s[:i] + '0' + s[i + 1:], 2))
            i += 1
        else:
            arr.append(int(s[:i] + '1' + s[i + 1:], 2))
            i += 1
    return arr

def te_check(s):
    i = 0
    while i < len(s):
        ans = 0
        if s[i] == '2':
            if int(s[:i] + '0' + s[i + 1:], 3) in bilist:
                return int(s[:i] + '0' + s[i + 1:], 3)
            elif int(s[:i] + '1' + s[i + 1:], 3) in bilist:
                return int(s[:i] + '1' + s[i + 1:], 3)
            else:
                i += 1
        elif s[i] == '0':
            if int(s[:i] + '1' + s[i + 1:], 3) in bilist:
                return int(s[:i] + '1' + s[i + 1:], 3)
            elif int(s[:i] + '2' + s[i + 1:], 3) in bilist:
                return int(s[:i] + '2' + s[i + 1:], 3)
            else:
                i += 1
        else:
            if int(s[:i] + '0' + s[i + 1:], 3) in bilist:
                return int(s[:i] + '0' + s[i + 1:], 3)
            elif int(s[:i] + '2' + s[i + 1:], 3) in bilist:
                return int(s[:i] + '2' + s[i + 1:], 3)
            else:
                i += 1

T = int(input())
for tc in range(1, T + 1):
    print('#{}'.format(tc), end=' ')
    bi = str(input())
    te = str(input())
    bilist = bi_cases(bi)
    print(te_check(te))
