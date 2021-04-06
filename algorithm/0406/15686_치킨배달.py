from itertools import combinations

N, M = map(int, input().split())
temp = [list(map(int, input().split())) for _ in range(N)]

house = [] # 집의 위치 list
chicken = [] # 치킨집의 위치 list
for i in range(N):
    for j in range(N):
        # 1,1 부터 시작이므로 좌표에 + 1
        if temp[i][j] == 1: # 집의 좌표 추가
            house.append([i + 1, j + 1])
        if temp[i][j] == 2: # 치킨집의 좌표 추가
            chicken.append([i + 1, j + 1])

total = [] # 도시의 치킨 거리 list
for choice in combinations(chicken, M): # 치킨집의 좌표 중 M개씩 선택한 조합
    city = [] # 치킨 거리 list
    # 한 집에서 M 개의 치킨집과의 최소 치킨거리 구하기
    for i in range(len(house)):
        minV = 100 # 최대 치킨 거리
        for j in range(M):
            # 최소 치킨 거리
            minV = min(minV, abs(choice[j][0] - house[i][0]) + abs(choice[j][1] - house[i][1]))
        city.append(minV)
    total.append(sum(city)) # 최소 치킨 거리의 합 = 도시의 치킨 거리
print(min(total)) # 최소 도시의 치킨 거리 출력