### [ 다익스트라 최단 경로 알고리즘 ]  ###

# 그래프
#   : 각 지점을 '노드'라 하고 지점간 연결된 로드를 '간선'이라고 표현한다.

# 다익스트라 알고리즘
# 그래프에서 여러 개의 노드가 존재할 때, 특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘
# 음의 간선이 없을때 정상적으로 작동한다.
# 매번 가장 비용이 적은 노드를 선택해서 임의의 과정을 반복한다.
# 따라서 그리디 알고리즘으로 분류된다.

# 원리
#   1) 출발 노드 설정
#   2) 최단 거리 테이블 초기화
#   3) 현재 노드에서 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드 선택
#   4) 해당 노드를 거쳐 다른 노드로 가는 각각의 비용을 계산하여 최단 거리 테이블 갱신
#   5) 3번과 4번과정을 반복한다.

# 소스코드 구현
## 방법1. ##
# 각 노드에 대한 최단 거리를 담는 1차원 리스트를 이용하기
# running time = O(n^)
import sys
input_data = sys.stdin.readline()
INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수 입력받기
n, m = map(int, input().split())
# 시작 노드의 번호
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)]
# 방문여부에 관한 체크표시 리스트
visited = [False]*(n+1)
# 각 노드에 대한 최단 거리 테이블을 무한값으로 초기화
distance = [INF]*(n+1)

# 모든 간선 정보 입력하기
for _ in range(m):
    a, b, c = map(int, input().split())     # a번 노드에서 b번 노드로 가는 비용이 c이다,
    graph[a].append((b,c))

# 방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0   # 최단 거리가 가장 짧은 노드의 인덱스
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i] :
            min_value = distance[i]
            index = i
    return index

# 다익스트라 알고리즘
def dijstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 n-1개 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 가는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# 알고리즘 수행하기
dijstra(start)

# 모든 노드로 가기 위한 최단 거리 출력하기
for i in range(1, n+1):
    # 도달할 수 없는 경우 무한이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])


## 방법 2.    : 개선된 다익스트라 알고리즘 ##
# running time : O(m*logn)
# 최단 거리가 가장 짧은 노드를 방법1에서처럼 선형적으로(모든 원소를 앞에서부터 하나씩)가 아닌 방법을 이용
# 힙 자료구조 이용

## [힙] ##
# 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 우선순위 큐를 구현하기 위해 사용되는 자료구조
# 라이브러리 지원
#   : PriorityQueue  혹은  heapq
# 우선순위 값을 표현하기  :  정수형 자료형의 변수 사용
# 우선순위 큐 라이브러리에 데이터의 묶음을 넣으면 첫 번째 원소를 기준으로 우선순위를 설정
# Min Heap  /  Max Heap
# 파이썬 라이브러리에서는 기본적으로 최소 힙 구조를 이용한다.
# 최소 힙에서 우선순위에 해당하는 값에 음수 부호를 붙였다가 나중에 큐에서 추출한 이후 다시 원래값으로 되돌리면 최대힙처럼 구현가능

# 최단 거리를 저장하기 위한 1차원 리스트(최단 거리 테이블)은 그대로 사용하고
# 현재 가장 가까운 노드를 저장하기 위한 목적으로만 우선순위 큐를 추가로 이용한다.

# 앞의 방법1에서의 get_smallest_node()라는 함수를 작성할 필요가 없다!
# 최단 거리가 가장 짧은 노드를 선택하는 과정을 다익스트라 최단 경로 함수 안에서 우선순위 큐를 이용하는 방식으로 대체!

import heapq
import sys
input_data = sys.stdin.readline
INF = int(1e9)

# 노드개수, 간선개수
n, m = map(int, input().split())
start = int(input())
# 각 노드의 정보 읽기
graph = [[] for _ in range(n+1)]
# 최단 거리 테이블 초기화
shortest_d = [INF] * (n+1)

# 모든 간선 정보 입력
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))     # a노드에서 b노드까지 경로 비용 c

# 다익스트라 최단 경로 알고리즘
def dijkstra(start):
    # 우선순위 큐를 위한 리스트 준비
    q = []
    # 시작지점 정보 입력하기
    shortest_d[start] = 0
    heapq.heappush(q, (0, start))
    while q:    # q가 비어있지 않을 때 까지
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내어 현재 노드로
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적 있는 노드라면 무시하기
        if shortest_d[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost =  dist + i[1]
            if cost < shortest_d[i[0]]:
                shortest_d[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

# 모든 노드로 가기 위한 최단거리 출력하기
for i in range(1, n+1):
    if shortest_d == INF:
        print('INFINITY')
    else:
        print(shortest_d[i])