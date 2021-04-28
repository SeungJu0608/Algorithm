## 왕실의 나이트
inputdata = input()
row = int(inputdata[1])
col = int(ord(inputdata[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 경우
steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

# 경우의 수
result = 0
for i in steps:
    # 이동하고자 하는 위치
    next_row = row + i[0]
    next_col = col + i[1]
    # 이동이 가능하다면 케이스 증가
    if 1 <= next_row <= 8 and 1 <= next_col <= 8:
        result += 1

print(result)

## 상하좌우 문제
n = int(input())
data = input().split()
x, y = 1, 1

# L, R, U, D 에 따른 이동방향
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
move_types = ['L', 'R', 'U', 'D']

for move in data:
    for i in range(len(move_types)):
        if move == i:
            next_x = x + dx[i]
            next_y = y + dy[i]
    if next_x < 1 and next_x > n and n < next_y < 1:
        continue
    x, y = next_x, next_y

print(x, y)

## 게임 개발
n, m = map(int, input().split())
A, B, d = map(int, input().split())
# direction = [N, E, S, W]
# 전체 맵정보 읽어들이기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 방문한 위치를 저장하기 위한 1로 체크표시
visited = [[0] * m for _ in range(n)]
d[x][y] = 1  # 현재 위치 표시

# direction 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# turn left
def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3


# start the simulation
count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]
    if visited[nx][ny] == 0 and array[nx][ny] == 0:
        x = nx
        y = ny
        visited[x][y] = 1
        count += 1
        turn_time = 0
    turn_time += 1
    if turn_time == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        break
    turn_time = 0

print(count)
