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

## 02. 문자열 재정렬
data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))

## 03. 문자열 압축
def solution(s):
    answer = len(s)

    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]
        count = 1

        for j in range(step, len(s), step):
            if prev == s[j:j + step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step]
                count = 1

        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))

    return answer

## 04. 자물쇠와 열쇠
def rotate_a_matrix_by_90_degree(a):
    n = len(a)
    m = len(a[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result

def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]

    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key)
        for x in range(n * 2):
            for y in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]

                if check(new_lock) == True:
                    return True

                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    return False

## 05. 뱀
n = int(input())
k = int(input())
data = [[0] * (n + 1) for _ in range(n + 1)]
info = []

for i in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1
    data[x][y] = 2
    direction = 0
    time = 0
    index = 0
    q = [(x, y)]

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 1 <= nx and nx <= n and 1 <= ny and data[nx][ny] != 2:
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0

            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))
        else:
            time += 1
            break

        x, y = nx, ny
        time += 1
        if index < l and time == info[index][0]:
            direction = turn(direction, info[index][1])
            index += 1
    return time

print(simulate())

## 06. 기둥과 보 설치
def possible(ans):
    for i in ans:
        x, y, type = i
        if type == 0:
            if y == 0 :
                continue
            if [x - 1, y, 1] in ans or [x, y, 1] in ans :
                continue
            if [x, y - 1, 0] in ans :
                continue
        else :
            if [x, y - 1, 0] in ans or [x + 1, y - 1, 0] in ans :
                continue
            if [x - 1, y, 1] in ans and [x + 1, y, 1] in ans :
                continue
        return False

    return True
def solution(n, build_frame):
    answer = []
    for i in build_frame:
        if i[3] == 0 :
            answer.remove([i[0], i[1], i[2]])

            if not possible(answer) :
                answer.append([i[0], i[1], i[2]])

        else :
            answer.append([i[0], i[1], i[2]])

            if not possible(answer):
                answer.remove([i[0], i[1], i[2]])

    answer.sort()
    return answer

## 07. 치킨 배달
from itertools import combinations

n , m = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(n)]
chicken , house = [] , []

for r in range(n):
    for c in range(n):
        if data[r][c] == 1:
            house.append((r,c))
        elif data[r][c] == 2:
            chicken.append((r,c))

candidates = list(combinations(chicken,m))

def get_sum(candidate):
    result = 0
    for hx,hy in house:
        temp = 1e9
        for cx,cy in candidate:
            temp = min(temp, abs(hx-cx) + abs(hy-cy))
        result += temp
    return result

result = 1e9
for candidate in candidates:
    result = min(result,get_sum(candidate))

print(result)

## 08. 외벽 점검
from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)

    for i in range(length):
        weak.append(weak[i] + n)
    answer = len(dist) + 1

    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            count = 1
            position = weak[start] + friends[count - 1]

            for index in range(start, start + length):
                if position < weak[index]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count)
    if answer > len(dist):
        return -1
    return answer

# 3. DFS/BFS
## 01. 특정 거리의 도시 찾기
from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n + 1)
distance[x] = 0
q = deque([x])

while q:
    now = q.popleft()

    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)

check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)

## 02. 연구소
n, m = map(int, input().split())
data = []
temp = [[0] * m for _ in range(n)]

for _ in range(n):
    data.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

def dfs(count):
    global result

    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]

        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)

        result = max(result, get_score())
        return

    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)