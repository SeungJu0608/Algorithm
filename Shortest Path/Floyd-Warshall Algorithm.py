### [ 플로이드 워셜 알고리즘 ] ###

# 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야하는 경우 사용할 수 있는 알고리즘
# cf) 다익스트라 알고리즘 : 한 노드에서 다른 특정 노드까지의 최단 경로를 구하는 경우 이용한다.
# Main Idea :
#   단계마다 거쳐 가는 노드를 기준으로 알고리즘을 수행하는데 매번 방문하지 않은 노드 중에서 최단 거리를 갖는 노드를 찾을 필요없음
#   노드의 개수가 N개일 때 알고리즘상으로 N번의 단계를 수행하며 단계마다 O(N^2)의 연산을 통해
#   현재 노드를 거쳐가는 모든 경로를 고려한다.
# running time : O(N^3)

# 2차원 리스트에 최단 거리 정보를 저장하여 모든 노드에 대해 다른 모든 노드로의 최단 거리 정보를 담는다.
# N개의 노드에 대해 N번 만큼의 단계를 반복하며 동일한 과정을 점화식에 맞게 수행하기 때문에 다이나믹 프로그래밍에 속한다.
# 각 단계에서는 해당 노드를 거쳐가는 경우를 고려한다.
#       e.g) 1번 노드 확인 == 1번 노드를 중간에 거쳐 지나가는 모든 경우 == (A -> 1 -> B)
# 따라서 알고리즘에서는 현재 확인하고 있는 노드를 제외하고 N-1개 중 서로다른 노드 두쌍을 선택한 후(A, B)
# A -> 1 -> B의 경로에 대한 최단 거리를 갱신한다.

# K번의 단계에 대한 점화식
#   :  D_ab = min(D_ab, D_ak + D_kb)

# 소스코드
INF = int(1e9)

# 노들의 개수, 간선의 개수
n = int(input())
m = int(input())
# 2차원 리스트 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0
## 혹은
## for i in range(1, n+1):
##      graph[i][i] = 0

# 각 간선에 대한 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())     # a노드에서 b노드로 비용 c
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        # 도달할 수 없는경우
        if graph[a][b] == INF:
            print('INFINITY', end='')
        else:
            print(graph[a][b], end='')
    print()

