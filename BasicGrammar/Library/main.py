# 주요 라이브러리의 문법과 유의점 #

# 1. 내장함수 : import 없이 바로 사용 가능
## 1-1. sum() : iterable; 반복 가능한 객체(리스트, 사전, 튜플 등)가 입력으로 주어지면 모든 원소의 합을 반환
result = sum([1, 2, 3, 4, 5])
print(result)

## 1-2. max() / min() : 파라미터가 2개 이상일 때 가장 큰/작은 값을 반환
result1 = max(7, 3, 5, 2)
result2 = min(7, 3, 5, 2)
print(result1)
print(result2)

## 1-3. eval() : 수식이 문자열로 들어오면 해당 수식의 결과를 반환
result = eval("(3 + 5) * 7")
print(result)

## 1-4. sorted() : iterable 객체가 들어왔을 때, 정렬된 결과를 반환
result = sorted([9, 1, 8, 5, 4])                    # 오름차순 정렬
print(result)
result = sorted([9, 1, 8, 5, 4], reverse = True)    # 내림차순 정렬
print(result)

## 1-5. sort() : iterable 객체는 기본적으로 sort() 함수를 내장하고 있음
data = [9, 1, 8, 5, 4]
data.sort()
print(data)

# 2. itertools : 반복되는 데이터를 처리하는 기능을 포함
## 2-1. permutations() : iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)를 계산
from itertools import permutations
data = ['A', 'B', 'C']  # r = 3
result = list(permutations(data, 3))    # 모든 순열 구하기
print(result)

## 2-2. combinations() : iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합)를 계산
from itertools import combinations
data = ['A', 'B', 'C']
result = list(combinations(data, 2))    # 2개를 뽑는 모든 조합 구하기
print(result)

## 2-3. product() : iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)를 계산
#                 : 단, 원소를 중복하여 뽑음
from itertools import product
data = ['A', 'B', 'C']
result = list(product(data, repeat=2))                  # 2개를 뽑는 모든 순열 구하기(중복 허용)
print(result)

## 2-4. combinations_with_replacement() : iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합)를 계산
#                                       : 단, 원소를 중복하여 뽑음
from itertools import combinations_with_replacement
data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data, 2))   # 2개를 뽑는 모든 조합 구하기(중복 허용)
print(result)

# 3. heapq
## 3-1. heapq.heappush() : 힙에 원소를 삽입
## 3-2. heapq.heappop() : 힙에서 원소를 꺼내기
import heapq

### 3-1-1. 오름차순 힙 정렬 구현
def heapsort(iterable):
    h = []
    result = []
    for value in iterable:          # 모든 원소를 차례대로 힙에 삽입
        heapq.heappush(h, value)
    for _ in range(len(h)):         # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
        result.append(heapq.heappop(h))
    return result

result = heapsort([1, 3, 5 ,7 ,9 , 2, 4, 6, 8, 0])
print(result)

### 3-1-2. 내림차순 힙 정렬 구현
def heapsort(iterable):
    h = []
    result = []
    for value in iterable:          # 모든 원소의 부호를 바꾸고 차례대로 힙에 삽입
        heapq.heappush(h, -value)
    for _ in range(len(h)):         # 힙에 삽입된 모든 원소를 차례대로 꺼내어  다시 원소의 부호를 바꾸고 담기
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1, 3, 5 ,7 ,9 , 2, 4, 6, 8, 0])
print(result)

# 4. bisect : 이진 탐색을 쉽게 구현, '정렬된 배열'에서 특정한 원소를 찾아야 할 때 매우 효과적
## 4-1. bisect_left(a, x)   : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
## 4-2. bisect_right(a, x)  : 정렬된 순서를 유지하도록 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4
print(bisect_left(a, x))    # 2
print(bisect_right(a, x))   # 4

### 4-1-1. 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
print(count_by_range(a, 4, 4))      # 2 → left_index = 6, right_index = 8
print(count_by_range(a, -1, 3))     # 6 → left_index = 0, right_index = 6

# 5. collections : 유용한 자료구조를 제공하는 라이브러리
## 5-1. deque() : 큐를 구현하는 메서드
#               : 인덱싱, 슬라이싱 사용 불가, 하지만 연속적으로 나열된 데이터의 시작 부분이나 끝 부분에 데이터를 삽입/삭제할 때 효과적
from collections import deque

data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)
print(list(data))   # 리스트 자료형으로 변환

## 5-2. Counter() : 등장 횟수를 세는 기능
#                 : iterable 객체가 주어졌을 때, 해당 객체 내부의 원소가 몇 번씩 등장했는지 알려줌
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(counter['red'])       # 'red' 등장 횟수
print(counter['blue'])      # 'blue' 등장 횟수
print(counter['green'])     # 'green' 등장 횟수
print(dict(counter))        # 사전 자료형으로 변환

# 6. math : 수학적인 기능을 포함한 라이브러리
import math

## 6-1. factorial(x) : x! 값을 반환
print(math.factorial(5))

## 6-2. sqrt(x) : x의 제곱근을 반환
print(math.sqrt(49))

## 6-3. gcd(x, y) : x와 y의 최대 공약수를 반환
print(math.gcd(21, 14))

## 6-4. pi(), e() : 파이나 자연상수 값을 반환
print(math.pi)
print(math.e)
