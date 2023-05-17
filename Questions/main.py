# 1. 그리디
## 01. 모험가 길드
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
count = 0

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)

## 02. 곱하기 혹은 더하기
data = input()
result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])

    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)

## 03. 문자열 뒤집기
data = input()
count0 = 0
count1 = 0

if data[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        if data[i + 1] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))

## 04. 만들 수 없는 금액
n = input()
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    if target < x:
        break
    target += x

print(target)

## 05. 볼링공 고르기
n, m = map(int, input().split())
data = list(map(int, input().split()))
array = [0] * 11

for x in data:
    array[x] += 1

    result = 0

for i in range(1, m + 1):
    n -= array[i]
    result += array[i] * n

print(result)

## 06. 무지의 먹방 라이브
import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    sum_value = 0
    previous = 0
    length = len(food_times)

    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop()
        sum_value += (now - previous) * length
        length -= 1
        previous = now

    result = sorted(q, key= lambda x: x[1])
    return result[(k - sum_value) % length][1]

# 2. 구현
## 01. 럭키 스트레이트
n = input()
length = len(n)
summary = 0

for i in range(length // 2):
    summary += int(n[i])

for i in range(length // 2, length):
    summary -= int(n[i])

if summary == 0:
    print("LUCKY")
else:
    print("READY")