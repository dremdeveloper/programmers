from collections import deque

#① 이동 가능한 좌표인지 판단하는 함수
def is_valid_move(ny, nx, n, m, maps):
    return 0 <= ny < n and 0 <= nx < m and maps[ny][nx] != 'X'

#② 방문한 적이 없으면 큐에 넣고 방문 여부를 표시한다.
def append_to_queue(ny, nx, k, time, visited, q):
    if not visited[ny][nx][k]:
        visited[ny][nx][k] = True
        q.append((ny, nx, k, time + 1))

def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[[False for _ in range(2)] for _ in range(m)] for _ in range(n)]
    #③ 위, 아래, 왼쪽, 오른쪽 이동 방향
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    q = deque()
    end_y, end_x = -1, -1
    
    #④ 시작점과 도착점을 찾아 큐에 넣고 방문 여부를 표시한다.
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                q.append((i, j, 0, 0))  # 시작점
                visited[i][j][0] = True
            if maps[i][j] == 'E':
                end_y, end_x = i, j   # 도착점
    
    while q:
        y, x, k, time = q.popleft()  #⑤ 큐에서 좌표와 이동 횟수를 꺼낸다.
        
        #⑥ 도착점에 도달하면 결과를 반환한다.
        if y == end_y and x == end_x and k == 1:
            return time
        
        #⑦ 4방향으로 이동해본다.
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            #⑥ 이동 가능한 좌표인 경우에만 큐에 넣는다.
            if not is_valid_move(ny, nx, n, m, maps):
                continue
            
            #⑧ 다음 이동 지점이 물인 경우
            if maps[ny][nx] == 'L':
                append_to_queue(ny, nx, 1, time, visited, q)
            #⑨ 다음 이동 지점이 물이 아닌 경우
            else:
                append_to_queue(ny, nx, k, time, visited, q)
    
    #⑩ 도착점에 도달하지 못한 경우
    return -1
