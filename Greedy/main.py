# 예제 3-1
n = 1260
count = 0

coin_types = [500, 100, 50, 10]

# 화폐의 종류(K)만큼 반복 수행... 시간 복잡도는 O(K)
for coin in coin_types:
    count += n // coin
    n %= coin

print(count)

# 문제 1. 큰 수의 법칙
n, m, k = map(int, input().split())     # N, M, K 공백으로 구분하여 입력받기
data = list(map(int, input().split()))  # N개의 수를 공백으로 구분하여 입력받기

data.sort()             # 입력받은 수 정렬
first = data[n - 1]     # 가장 큰 수
second = data[n - 2]    # 다음으로 큰 수

result = 0

while True:
    for i in range(k):  # 가장 큰 수를 k번 더하기
        if m == 0:      # m == 0이면 반복문 탈출
            break
        result += first
        m -= 1          # 덧셈을 수행할 때마다 m을 1씩 감소
    if m == 0:
        break
    result += second    # 두 번째로 큰 수를 한 번 더하기
    m -= 1              # 덧셈을 수행할 때마다 m을 1씩 감소

print(result)           # 최종 답안 출력

# 문제 2. 숫자 카드 게임
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)

# 문제 3. 1이 될 때까지
n, k = map(int, input().split())
result = 0

while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1

while n > 1:
    n -= 1
    result += 1

print(result)