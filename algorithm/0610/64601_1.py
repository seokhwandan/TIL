def solution(board, moves):
    answer = 0
    basket = []
    for k in moves:
        for bd in board:
            if bd[k - 1]:
                basket.append(bd[k - 1])
                bd[k - 1] = 0
                break
            if len(basket) >= 2 and basket[-1] == basket[-2]:
                basket = basket[:-2]
                answer += 2
    return answer

a = solution([[0,0,0,0,0], [0,0,1,0,3], [0,2,5,0,1], [4,2,4,4,2], [3,5,1,3,1]], [1,5,3,5,1,2,1,4])
print(a)