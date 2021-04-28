from collections import deque

## 음료수 얼려먹기
# DFS 이용
graph = [[0, 0, 1],
         [0, 1, 0],
         [1, 0, 1]]


def dfs(x, y):
    if -1 >= x or x >= 3 or -1 >= y or 3 <= y:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1  # 방문처리
        dfs(x - 1, y)  # 인접 위치 재귀적 호출
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


result = 0
for i in range(3):
    for j in range(3):
        if dfs(i, j) is True:
            result += 1

print(result)

## 미로 탈출
# BFS 알고리즘을 이용하기
# 큐 자료구조 이용
# import collections package on the top of the file for using deque library
# 데이터 입력
n, m = map(int, input().split())
maze_graph = []
for i in range(n):
    maze_graph.append(list(map(int, input())))

# 방향 정의하기(n by m matrix, up down left right)
dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]

# BFS
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복
    while queue:
        queue.popleft((x, y))
        # 네방향 하나씩 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 공간(graph)를 벗어난 경우 무시하기/ 벽면인 경우도 무시하기
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방분하는 경우에만 최단거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]

# BFS를 수행한 결과 출력
print(bfs(0,0))