## 1. 거스름돈
# 음식점의 계산을 도와주는 점원이 손님에게 거슬러주어야 할 돈이 N원일 때 거슬러 줘야할 동전의 최소개수를 구하여라.
# 사용할 거스름돈 동전으 500원, 100원, 50원, 10원으로 무한히 존재한다고 가정한다
n = 2570
count = 0
# 큰 단위의 화폐부터 차례로 확인
coins = [500, 100, 50, 10]  # 큰단위가 작은단위의 배수형태

for coin in coins:
    count += n // coin  # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 차례로 세기
    n %= coin

print(count)

## 2. 배열의 크기 = N , 숫자가 더해지는 총 횟수 = M , 배열의 특정한 인덱스에 해당하는 수가 연속 K번 초과하여 덧셈불가의 경우
# 주어진 배열의 수들을 M번 더하여 가장 큰 수를 만드는 법칙
# n,m,k 공백으로 구분하는 입력받기
n, m, k = map(int, input().split())
# n개의 수를 공백으로 구분하여 입려받기
data = list(map(int, input().split()))

data.sort()     # 입력받은 수를 정렬하기
max_value = data[n-1]
second = data[n-2]

# 수열 이용하기
# 반복되는 수열의 길이 = k+1
# 수열의 반복 횟수 = m//(k+1)
# 가장 큰 수가 더해지는 횟수
t = m//(k+1)*k + m % (k+1)

result = 0
result += t*max_value
result += (m-t)*second

print(result)


## 3. 숫자 카드 게임
# 여러 개의 숫자카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임
# 룰 : 1) 행렬의 형태로 카드들이 놓여있다. N by M
#     2) 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택
#     3) 선택된 행에 포함된 카드들 중 가장 낮은 숫자의 카드를 뽑는다
#     4) 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세운다.

n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)  # 가장 작은 수들 중에서 가장 큰수 찾기

print(result)

## 4. 1이 될 떄까지
# 어떤 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하는 횟수의 최솟값을 출력한다.
#   1) N에서 1을 뺀다
#   2) N을 K로 나눈다. 단, 이연산은 N이 K로 나누어 떨어질 떄만 선택 할 수 있다.
n, k = map(int, input().split())
result = 0

while True:
    # n이 k로 나누어 떨어질떄 까지 1빼기
    target = (n//k) * k
    result += (n - target)
    n = target
    # n이 k보다 작을 때 더이상 나눌수 없다. 따라서 반복문 탈출
    if n < k:
        break
    # k로 나누기
    n //= k
    result += 1

# 남은 수에 대해 1씩 빼기
result += (n-1)
print(result)
