import sys
sys.stdin = open('1244.txt')

def dfs(cnt):
    global ans
    if cnt == int(M): # 주어진 횟수만큼 교환했다면
        temp = int(''.join(num)) # list 형태를 숫자로 변환
        ans = max(ans, temp) # 더 큰 값으로 ans 갱신
        return

    for i in range(len(num)): 
        for j in range(i + 1, len(num)):
            num[i], num[j] = num[j], num[i] # 두개의 위치를 바꾸고
            value = ''.join(num) # value 에 str 형태로 저장
            if visited.get((value, cnt + 1), 1): # (value, cnt + 1) 을 key로 하는 value 값이 있으면 기존 value 반환, 없으면 1 반환
            # vistied 는 빈 dictionary 이므로 방문하지 않았으면 1을 반환
            # 즉 방문하지 않았을 때 if문 실행
                visited[(value, cnt + 1)] = 0 # 방문했으니 value 를 0으로
                dfs(cnt + 1) # 재귀
            num[i], num[j] = num[j], num[i] # 위치 원상복귀

T = int(input())
for t in range(1, T + 1):
    N, M = input().split()
    num = list(N)
    visited = {} # 방문체크 
    ans = 0
    dfs(0)
    print('#{} {}'.format(t, ans))