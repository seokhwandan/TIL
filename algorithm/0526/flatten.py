import sys
sys.stdin = open('flatten.txt')

for t in range(1, 11):
    dump = int(input())
    box = list(map(int, input().split()))
    res = 0
    cnt = 1
    while cnt <= dump:
        for i in range(99, 0, -1):
            for j in range(i):
                if box[j] > box[j + 1]:
                    box[j], box[j + 1] = box[j + 1], box[j]
        box[-1] -= 1
        box[0] += 1
        cnt += 1
        if box[-1] - box[0] == 0:
            res = 0
            break
        elif box[-1] - box[0] == 1:
            res = 1
            break
    for i in range(99, 0, -1):
            for j in range(i):
                if box[j] > box[j + 1]:
                    box[j], box[j + 1] = box[j + 1], box[j]
    res = box[-1] - box[0]
    print('#{} {}'.format(t, res))
