def solution(prices):
    n = len(prices)
    answer = [0] * n  #① 가격이 떨어지지 않은 기간을 저장할 배열
    
    # 스택(stack)을 사용하여 이전 가격과 현재 가격을 비교합니다.
    stack = [0]  #② 스택 초기화
    for i in range(1, n):
        while stack and prices[i] < prices[stack[-1]]:
            #③ 가격이 떨어졌으므로 이전 가격의 기간을 계산합니다.
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    #④ 스택에 남아 있는 가격들은 가격이 떨어지지 않은 경우입니다.
    while stack:
        j = stack.pop()
        answer[j] = n - 1 - j
    return answer
