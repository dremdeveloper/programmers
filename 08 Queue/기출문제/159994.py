def solution(cards1, cards2, goal):
    #① goal의 문자열을 순차적으로 순회 
    for _ in range(len(goal)):
        if len(cards1) > 0 and cards1[0] == goal[0]: # ② card1의 front와 일치하는 경우
            cards1.pop(0)
            goal.pop(0)
        elif len(cards2) > 0 and cards2[0] == goal[0]:# ③ card2의 front와 일치하는 경우
            cards2.pop(0)
            goal.pop(0)
    return "Yes" if len(goal) == 0 else "No"  # ④ goal이 비었으면 Yes 아니면 No를 반환
