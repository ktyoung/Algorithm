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