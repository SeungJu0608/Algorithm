### 부품찾기
# 각 고유한 정수 형태의 번호가 있는 부품 N개가 있다.
# 한 고객이 M개의 종류의 부품을 대량으로 구매하려한다. 이때 주문이 들어온 M개의 부품들을 확인하여 견적서를 작성한다.
# 고객이 요청한 부품 번호의 순서대로 확인해 부품이 있으면 yes, 없으면 no를 출력한다.

# 데이터 입력
# 총 부품개수 N
n = int(input())
# 매장 부품 리스트
stock_data = list(map(int, input().split()))
# 주문 수량
m = int(input())
# 주문 리스트
ordered_data = list(map(int, input().split()))

# 매장 부품 정렬
stock_data.sort()


# binary search
def bs_for_order(array, target, start, end):
    while start < end:
        mid = (start + end) / 2
        if array[mid] < target:
            return bs_for_order(array, target, start, mid - 1)
        if array[mid] > target:
            return bs_for_order(array, target, mid + 1, end)
        if array[mid] == target:
            return mid
    return None


# 요청한 부품 번호를 하나씩 확인
for i in ordered_data:
    result = bs_for_order(stock_data, i, 0, n)
    if result == None:
        print('no', end='')
    else:
        print('yes', end='')


# 데이터의 개수가 1,000,000을 넘지 않아 <계수 정렬> 이용할 수 있다.
# 모든 원소의 번호를 포함할 수 있는 크기의 리스트 만들기
sorted_list = [0] * 1000001  # 0포함 1,000,000까지의 인덱스

# 매장 재고로 남아있는 부품 번호 기록
for i in stock_data:
    sorted_list[i] = 1

# 고객이 주문한 부품 확인
for j in ordered_data:
    if sorted_list[j] == 1:
        print('yes', end='')
    else :
        print('no', end='')

# <집합 자료형> 이용하기
# 단순히 특정한 수가 한번이라도 등장했는지를 검사하면 된다. 따라서 집합 자료형을 이용할 수 있다.
# 집합 자료형 초기화하기 : set()함수 이용
# 집합 차료형으로 재고 데이터 입력
stock_set = set(map(int, input().split()))

# 주문 데이터 확인하기
for i in ordered_data:
    if i in stock_set:
        print('yes', end='')
    else:
        print('no', end='')



### 떡볶이 떡 만들기
# 길이가 일정하지 않은 가게의 떡볶이 떡과 봉지 안에 들어 가는 떡을 동일하게 절단하여 맞춘다.
# 절단기 높이 : H
# 절단기의 높이보다 긴 떡은 H위의 부분이 잘리고 낮은 떡은 잘리지 않는다.
# 고객은 잘린 떡의 총 길이 만큼의 떡을 가져간다.
# 고객이 요청한 떡의 총 길이 : M
# 적어도 M 만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구한다.

# 데이터 입력
n, m = list(map(int, input().split()))
dd_height = list(map(int, input().split))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = map(dd_height)

# 이진 탐색 반복 수행
machine_h = 0
while(start <= end):
    total = 0
    mid = (start + end) / 2
    for x in dd_height:
        if x > mid:
            total += (x - mid)
    if total < m:
        end = mid - 1
    else:    # if total >= m
        machine_h = mid  # 적어도 m 만큼의 떡을 가져가야하므로 result에 기록
        start = mid + 1

print(result)