import sys
sys.stdin = open('4866.txt')

T = int(input())
for t in range(1, T + 1):
    print('#{}'.format(t), end=' ')
    text = input()
    arr = []
    for i in text:
        if i == '(' or i ==')' or i == '{' or i == '}':
            arr.append(i)
    res = []
    for i in arr:
        res.append(i)
        if len(res) >= 2:
            if res[-2] == '(' and res[-1] == ')':
                res = res[:-2]
            elif res[-2] == '{' and res[-1] == '}':
                res = res[:-2]
    if res:
        print(0)
    else:
        print(1)
            