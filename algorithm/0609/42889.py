def solution(N, stages):
    answer = []

    stages = sorted(stages)

    my_dict = {}
    for i in range(1,N+1):
        my_dict.update({i:0})
    
    my_len = len(stages)

    for i in range(len(stages)):
        my_num = stages[i]

        if my_num > N:
            break

        over = 0

        if my_dict.get(my_num) != 0:
            continue
        else:
            over = my_len
            my_len -= stages.count(my_num)   
            if stages.count(my_num) != 0:
                fail = stages.count(my_num) / over
                my_dict.update({my_num:fail})

    my_dict = sorted(my_dict.items(), key = lambda x: x[1], reverse=True)

    for i in my_dict:
        answer.append(i[0])
    return answer

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))