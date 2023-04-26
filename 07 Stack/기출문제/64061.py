def solution(board, moves):
    #① 각 열에 대한 스택을 생성합니다.
    lanes = [[] for _ in range(len(board[0]))]

    #② board를 역순으로 탐색하며, 각 열의 인형을 lanes에 추가합니다.
    for i in range(len(board)-1, -1, -1):
        for j in range(len(board[0])):
            if board[i][j]:
                lanes[j].append(board[i][j])

    #③ 인형을 담을 바구니를 생성합니다.
    bucket = []

    #④ 사라진 인형의 총 개수를 저장할 변수를 초기화합니다.
    answer = 0

    #⑤ moves를 순회하며, 각 열에서 인형을 뽑아 bucket에 추가합니다.
    for m in moves:
        if lanes[m-1]: # 해당 열에 인형이 있는 경우
            doll = lanes[m-1].pop()

            if bucket and bucket[-1] == doll: #⑥ 바구니에 인형이 있고, 가장 위에 있는 인형과 같은 경우
                bucket.pop() 
                answer += 2 
            else: # ⑦ 바구니에 인형이 없거나, 가장 위에 있는 인형과 다른 경우
                bucket.append(doll) 

    return answer
