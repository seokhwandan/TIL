import sys
sys.stdin = open('5644.txt')

def charge(ar, ac, br, bc):
    maxV = 0 # 최대 충전량
    if not field[ar][ac]: # A 의 위치에서 충전이 되지 않을 때
        for b in field[br][bc]: # B 의 위치에서 충전이 가능하다면
            maxV = max(maxV, p[b]) # maxV = 파워가 큰 값
    elif not field[br][bc]: # B의 위치에서 충전이 되지 않을 때
        for a in field[ar][ac]: # A 의 위치에서 충전이 가능하다면
            maxV = max(maxV, p[a]) # 기존의 maxV = 파워가 큰 값

    for a in field[ar][ac]:
        for b in field[br][bc]:
            if a == b: # A 의 위차와 B 의 위치에서 같은 충전소를 공유할 때
                maxV = max(maxV, p[a]) # 반씩 나눠 충전하므로 결국 하나만 더하면 되고, 그 중 최댓값 찾기
            else: # 다르다면,
                maxV = max(maxV, p[a] + p[b]) # 둘 다 충전할 수 있으므로, 파워를 더하고 최대값 찾기
    return maxV

move = {
    0: (0, 0),
    1: (-1, 0),
    2: (0, 1),
    3: (1, 0),
    4: (0, -1)
}

T = int(input())
for t in range(1, T + 1):
    M, A = map(int, input().split()) # M : 이동시간, A : BC의 갯수
    a = list(map(int, input().split())) # A의 이동 경로
    b = list(map(int, input().split())) # B의 이동 경로
    field = [[[] for _ in range(10)] for _ in range(10)] # 10x10 field
    chargeV = 0 # 모든 경로 충전 결과
    p = {} # 파워 arr
    for i in range(A):
        c, r, C, P = map(int, input().split()) # bcr, bcc : bc의 y, x 좌표, C : 충전 범위, P : 충전 성능
        c, r = c - 1, r - 1
        p[i] = P # i 번 bc의 파워
        for j in range(10):
            for k in range(10):
                if abs(c - k) + abs(r - j) <= C:
                    field[j][k].append(i) # 충전 범위에 bc번호를 리스트로 추가

    chargeV += charge(0, 0, 9, 9)
    ar, ac, br, bc = 0, 0, 9, 9
    for i in range(M): # 경로를 이동할때마다 최대 충전량 더해주기
        ar += move[a[i]][0]
        ac += move[a[i]][1]
        br += move[b[i]][0]
        bc += move[b[i]][1]
        chargeV += charge(ar, ac, br, bc)
    print('#{} {}'.format(t, chargeV))