def solution(participant, completion):
    #① 해시테이블을 생성합니다.
    dic = {}
    
    #② 참가자들의 이름을 해시테이블에 추가합니다.
    for p in participant:
        if p in dic:
            dic[p] += 1
        else:
            dic[p] = 1
    
    #③ 완주한 선수들의 이름을 해시테이블에서 제거합니다.
    for c in completion:
        dic[c] -= 1
        
    #④ 해시테이블에 남아있는 선수가 완주하지 못한 선수입니다.
    for key in dic.keys():
        if dic[key] > 0:
            return key
