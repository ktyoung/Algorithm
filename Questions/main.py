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