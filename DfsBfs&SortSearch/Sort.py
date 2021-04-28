## Sort Algorithms
# 1) Selection Sort
# select the smallest item and change everytime
# running time : O(N^2) because of double loop
N = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(N)):
    min_index = i  # 가장 작은 원소의 인덱스
    for j in range(i+1, len(N)):
        if N[min_index] > N[j]:
            min_index = j
    N[i], N[min_index] = N[min_index], N[i]  # swape

print(N)


# 2) Insertion Sort
# 삽입 정렬은 선택 정렬보다는 효율적이지만 데이터가 거의 정렬 되어 있을때 훨씬 효율적이다.
# 특정한 데이터를 적절한 위치에 삽입한다는 의미
# 특정 데이터가 적절한 위치에 삽입되기 이전에 그 앞까지의 데이터는 이미 정렬되어 있다고 가정한다.
M = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 첫번째 데이터는 그 자체로 정렬이 되어있다고 판단한다.
for i in range(1, len(M)):
    for j in range(i, 0, -1):  # or for j in reversed(range(i+1))
        if M[j] > M[j-1]:
            M[j], M[j-1] = M[j-1], M[j]
        break
        # 정렬이 이루어진 원소는 항상 오름차순을 유지하고 있다. 따라서 특정 데이터가 삽입될 위치를 찾기 위해 한칸씩 왼쪽으로 이동할 때
        # 삽입될 데이터보다 작은 데이터를 만나면 그 위치에서 멈춘다.
print(M)

# 삽입 정렬은 최선의 경우 O(N)의 수행시간을 지닌다.
# 따라서 데이터가 거의 정렬이 되어 있는 경우 퀵 정렬 등의 다른 정렬 알고리즘을 이용하는 것보다 유리할 것 이다.

# 3) Quick Sort
# pivot : 큰 숫자와 작은 숫자를 교환하기 위한 기준. 미리 명시 필요함
# 가장 대표적인 방식 : Hoare Partition
#                   - list에서 가장 첫번째 데이터를 핏벗으로 정한다.
#                   - 이후 왼쪽에서부터 피벗보다 큰 데이터를 찾고, 오른쪽에서부터 피벗보다 작은 데이터를 찾아 두 데이터 위치 교환
#                   - 왼쪽에서 오는 값과 오른쪽에서부터 찾는 값의 위치가 서로 엇갈린 경우 작은 데이터와 피벗을 교환
#                   - 피벗이 이동한 상태에서 왼쪽 리스트와 오른쪽 리스트로 분할
#                   - 각 파티션을 각각 피벗을 설정하여 개별적으로 정렬 ( 재귀함수 동작 )
#                   - 이미 자료가 정렬되어 있는 경우에는 매우 느리게 작동
D = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    # 원소가 1개인 경우 종료
    if start >= end:
        return
    # 피벗 : 특정 원소의 인덱스 (여기서는 첫번째 원소를 기준으로 하므로 0)
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때 까지
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때 까지
        while right > start and array[right] >= array[pivot]:
            right -= 1
        # 두 동선이 겹칠 경우 pivot과 작은 데이터 swape
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        # 두 동선이 엇갈리지 않을 경우 두 데이터를 swape
        array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽과 오른쪽 각각 정렬진행 ( 재귀호출 )
    quick_sort(array, start, right-1)
    quick_sort(array, right + 1, end)


quick_sort(D, 0, len(D)-1)
print(D)

# 또는 파이썬의 장점을 살려 짧게 작성할 수 있다.
# 그러나 피벗과 데이터를 비교하는 연산횟수가 증가해 수행시간 면에서는 조금 비효율적이다.


def quick_sort(array):
    # list가 하나 이하의 원소만을 가지고 있다면 종료
    if len(array) <= 1:
        return
    # pivot = 첫번째 원소
    pivot = array[0]
    rest = array[1:]

    left_partition = [x for x in rest if x <= pivot]  # 분할 된 왼쪽 부분
    right_partition = [x for x in rest if x >= pivot]  # 분할 된 오른쪽 부분

    # 분할 이후 각 파티션 정렬과 병합
    return quick_sort(left_partition) + [pivot] + quick_sort(right_partition)


print(quick_sort(D))


# 4) Count Sort
# 특정 조건이 부합할 때만 사용 가능한 알고리즘
# 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때만 사용 가능
# 데이터의 모든 범위를 담을 수 있는 크기의 리스트를 선언해 주어야 하기 때문에 데이터의 가장 작은 값과
# 가장 큰 값의 차이가 1,000,000을 넘지 않을 떄 효과적으로 사용할 수 있다.
# 데이터의 개수 : N / 데이터 중 최대값 : K   =>  최악의 경우에도 running time = O(N+k)
# 비교 기반의 정렬 알고리즘이 아님
# 별도의 리스트를 선언하고 그 안에 정렬에 대한 정보를 담는다!

data = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

sorted_list = [0] * (max(data) - min(data) + 1)

for i in range(len(data)):
    # 해당하는 인덱스값 1씩 증가
    sorted_list[data[i]] += 1

for j in range(len(sorted_list)):
    for count in range(sorted_list[j]):
        print(j, end='')


## 파이썬 정렬 라이브러리
# 파이썬의 기본 정렬 라이브러리로 Merge Sort 방식을 기반으로 한 sorted() 함수를 제공한다.
# 리스트 객체 내부 함수인 sort()이용하면 별도의 정렬된 리스트가 반환되지 않고 내부 원소가 바로 정렬된다.
