def solution(id_list, report, k):
    reported_user = {} #신고 당한 사람, 신고자
    count = {} #받은 메일 개수
#① 신고 기록 순회
    for r in report:
        user_id, reported_id = r.split()
        if reported_id not in reported_user: #② 이전에 신고당한 기록이 없다면
            reported_user[reported_id] = set()
        reported_user[reported_id].add(user_id) #③ 신고 당한 사람의 아이디에 신고한 사람의 아이디를 기록
    for reported_id, user_id_lst in reported_user.items():
        if len(user_id_lst) >= k: #④ 정지 기준을 만족하면
            for uid in user_id_lst: #⑤ 신고한 사람에게 메일을 보낸다.
                if uid not in count:
                    count[uid] = 1
                else:
                    count[uid] += 1
    answer = []
    for i in range(len(id_list)): #⑥ 각 아이디별 메일 받은 횟수를 순서대로 정리
        if id_list[i] not in count:
            answer.append(0)
        else:
            answer.append(count[id_list[i]])
    return answer
