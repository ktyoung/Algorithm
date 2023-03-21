# 스택

# 5-1. 스택 예제
stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
print(stack[::-1])

# 5-2. 큐 예제
from collections import  deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)

# 5-3. 재귀 함수 예제
def recursive_function() :
    print("재귀 함수를 호출합니다.")
    recursive_function()

recursive_function()

# 5-4. 재귀 함수 종료 예제
def recursive_function(i) :
    if i == 100:
        return
    print(i, "번째 재귀 함수에서", i + 1, "번째 재귀 함수를 호출합니다.")
    recursive_function(i+1)
    print(i, "번째 재귀 함수를 종료합니다.")

recursive_function(1)

# 5-5. 2가지 방식으로 구현한 팩토리얼 예제
def factorial_interative(n) :
    result = 1
    for i in range(1, n + 1) :
        result *= i
    return result

def factorial_recursive(n) :
    if n <= 1 :
        return 1

    return n * factorial_recursive(n - 1)

print("반복적으로 구현:", factorial_interative(5))
print("재귀적으로 구현:", factorial_recursive(5))

# 5-6. 인접 행렬 방식 예제
INF = 99999999

graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph)

# 5-7. 인접 리스트 방식 예제
graph = [[] for _ in range(3)]

graph[0].append((1, 7))
graph[0].append((2, 5))

graph[1].append((0, 7))

graph[2].append((0, 5))

print(graph)

# 5-8. DFS 예제
def dfs(graph, v, visited) :
    visited[v] = True
    print(v, end=' ')

    for i in graph[v] :
        if not visited[i] :
            dfs(graph, i, visited)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

dfs(graph, 1, visited)

# 5-9. BFS 예제
from collections import deque

def bfs(graph, start, visited) :
    queue = deque([start])
    visited[start] = True
    while queue :
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
visited = [False] * 9

bfs(graph, 1, visited)