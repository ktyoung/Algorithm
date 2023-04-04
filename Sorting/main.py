# 6-1. 선택 정렬 소스코드
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)) :
    min_index = i
    for j in range(i + 1, len(array)) :
        if array[min_index] > array[j] :
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)

# 6-3. 삽입 정렬 소스코드
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)) :
    for j in range(i, 0, -1) :
        if array[j] < array[j -1] :
            array[j], array[j -1] = array[j - 1], array[j]
        else:
            break

print(array)

# 6-4. 퀵 정렬 소스코드
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end) :
    if start >= end :
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right :
        while left <= end and array[left] <= array[pivot] :
            left += 1
        while right > start and array[right] >= array[pivot] :
            right -= 1

        if left > right :
            array[right], array[pivot] = array[pivot], array[right]
        else :
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)

# 6-5. 퀵 정렬 소스코드(파이썬)
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array) :
    if len(array) <= 1 :
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))

# 6-6. 계수 정렬 소스코드
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(array) + 1)

for i in range(len(array)) :
    count[array[i]] += 1

for i in range(len(count)) :
    for j in range(count[i]) :
        print(i, end=" ")

# 6-7. sorted 소스 코드
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

result = sorted(array)
print(result)

# 6-8. sort 소스코드
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

array.sort()
print(array)

# 6-9. 정렬 라이브러리에서 key를 활용한 소스코드
array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data) :
    return data[1]

result = sorted(array, key=setting)
print(result)

# 실전 문제 2. 위에서 아래로
n = int(input())

array = []
for i in range(n) :
    array.append(int(input()))

array = sorted(array, reverse=True)

for i in array :
    print(i, end=" ")

# 실전 문제 3. 성적이 낮은 순서로 학생 출력하기
n = int(input())

array = []
for i in range(n) :
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

array = sorted(array, key=lambda student : student[1])

for student in array :
    print(student[0], end=' ')


# 실전 문제 4. 두 배열의 원소 교체
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k) :
    if a[i] < b[i] :
        a[i], b[i] = b[i], a[i]
    else :
        break

print(sum(a))