## list 내에서 데이터를 빠르게 탐색하는 이진 탐색 알고리즘 ##

# <Sequential Search>
# 가장 기본 탐색 방법
# 리스트 내부의 특정 데이터를 찾기위해 앞에서부터 하나씩 차례대로 확인하는 방법
# count() 메서드의 내부에서도 순차 탐색이 이루어진다
# running time = O(N)
# 순차 탐색의 구현
def sequential_search(target, data_list):
    for i in range(len(data_list)):
        if data_list[i] == target:
            return i + 1   # target의 위치를 반환


# <Binary Search>
# 배열 내부의 데이터가 정렬되어 있어야만 사용 가능하다.
# 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 특징이 있다.
# 변수 : 시작점 / 끝점 / 중간점
# 타겟이 되는 데이터와 중간점에 있는 데이터를 반복적으로 비교하여 탐색한다.
# running time = O(logN)
# Binary Search의 구현
# 1) 재귀 함수의 활용
def BS(data_list, target, start_indx, end_indx):
    mid = (start_indx + end_indx) / 2
    if target < data_list[mid]:
        return BS(data_list, target, start_indx, mid - 1)
    if target > data_list[mid]:
        return BS(data_list, target, mid + 1, start_indx)
    if target == data_list[mid]:
        return mid


# 2) 반복문을 활용
def BS(data_list, target, start_index, end_index):
    while start_index < end_index:
        mid_index = (start_index + end_index) / 2
        if target < data_list[mid_index]:
            end_index = mid_index - 1
        if target > data_list[mid_index]:
            start_index = mid_index + 1
        if target == mid_index:
            return mid_index
    return None

