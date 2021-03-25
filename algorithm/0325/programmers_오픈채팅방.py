def solution(record):
    answer = []
    dic = {}
    # .split 을 통해 단어 사이의 공백을 기준으로 나누고,
    # 딕셔너리의 키값을 id, 밸류값을 닉네임을 넣어주었다.
    # 채팅방 안에서 닉네임을 바꾸거나 나가서 바꾸고 오게되면 전 닉네임이 새로운 닉네임으로 바뀌게 되기 때문에
    # 마지막 닉네임만 저장하면 된다.
    for r in record:
        if r.split(' ')[0] == 'Enter' or r.split(' ')[0] == 'Change':
            dic[r.split(' ')[1]] = r.split(' ')[2]
    
    # Enter 와 Leave 에 따라 딕셔너리의 키값인 아이디에 해당하는 밸류값 닉네임을 받았고,
    # Enter 와 Leave 에 해당하는 문자열을 answer 리스트에 추가하였다.
    for r in record:
        if r.split(' ')[0] == 'Enter':
            answer.append(dic[r.split(' ')[1]] + '님이 들어왔습니다.')
        elif r.split(' ')[0] == 'Leave':
            answer.append(dic[r.split(' ')[1]] + '님이 나갔습니다.')
    
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
answer = []
solution(record)
print(answer)