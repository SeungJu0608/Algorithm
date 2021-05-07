### < Heap Sort > ###
# heap 기능을 위해 heapq 라이브러리를 사용
# heapq는 다양한 알고리즘에서 우선순위 큐 기능을 구현하고자 할 때 사용된다.
# 힙 정렬 구현하기
import heapq

def heapsort(iterable):
    h =[]
    result = []
    # 모든 원소를 차례대로 힙에 삽입하기
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 우선순위대로 차례로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result
