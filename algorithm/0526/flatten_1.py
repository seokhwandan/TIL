import sys
sys.stdin = open('flatten.txt')

for t in range(1, 11):
    dump = int(input())
    box = list(map(int, input().split()))
    res = 0
    cnt = 1
    while cnt <= dump:
        box.sort()
        box[-1] -= 1
        box[0] += 1
        cnt += 1
        if box[-1] - box[0] == 0:
            res = 0
            break
        elif box[-1] - box[0] == 1:
            res = 1
            break
    box.sort()
    res = box[-1] - box[0]
    print('#{} {}'.format(t, res))