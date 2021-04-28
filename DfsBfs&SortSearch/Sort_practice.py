### up to down
# 수열을 내림차순으로 만드는 프로그램 만들기
# 데이터 입력
n = int(input())
data = []
for i in range(n):
    data.append(int(input()))

# 내림차순으로 정렬하기
# 모든 수는 1 이상 100,000 이하이므로 어떠한 정렬 알고리즘을 써도 무방함
# 가장 간단한 기본 정렬 라이브러리를 이용한다.
data = sorted(data, reverse=True)

# 정렬이 된 결(과를 공백으로 구분하여 출력
for i in data:
    print(i, end='')


### 성적이 낮은 순서대로 학생 출력하기
# 데이터 입력
n = int(input())
array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

# 점수를 기준으로 정렬 (key 이용)
array = sorted(array, key=lambda student: student[1])

# 정렬이 수행된 결과를 출력 (학생이름을 출력)
for student in array:
    print(student[0], end='')


### 두 배열의 원소 교체
# 두 배열 A,B는 N개의 자연수로 되어있고 최대 K번 바꿔치기 연산 수행가능
# 최종 목표 : 배열 A의 모든 원소의 합이 최대가 되도록 한다.
# A는 오름차순으로 B는 내림차순으로 정렬 후 바꾸기
n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A = sorted(A)
B = sorted(B, reverse=True)

for i in range(n):
    if A[i] < B[i] and i <= k-1:
        A[i], B[i] = B[i], A[i]
    break
# 또는
# for i in range(k):
#   if A[i] < B[i]:
#       A[i], B[i] = B[i], A[i]

print(sum(A))


