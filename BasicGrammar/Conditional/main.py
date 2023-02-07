# 조건문 #
# 1. if문
x = 15
if x >= 10:
    print(x)

# 2. if ~ elif ~ else문
score = 85
if score >= 90:
    print("학점 : A")
elif score >= 80:
    print("학점 : B")
elif score >= 70:
    print("학점 : C")
else:
    print("학점 F")

# 3. 비교 연산자
x = 10
y = 20

if x == y:
    print("x와 y는 서로 같습니다.")
if x != y:
    print("x와 y는 서로 다릅니다.")
if x > y:
    print("x는 y보다 큽니다.")
if x >= y:
    print("x는 y보다 크거나 같습니다.")
if x < y:
    print("x는 y보다 작습니다.")
if x <= y:
    print("x는 y보다 작거나 같습니다.")

# 4. 논리 연산자
x = True
y = False
if x and y:
    print("X와 Y가 True입니다.")
if x or y:
    print("X나 Y 중 하나가 True입니다.")
if not x:
    print("X는 False입니다.")

# 5. 기타 연산자
## 5-1. in / not in 연산자
data = [1, 2, 3, 4, 5]
if 3 in data:       # 3이 리스트(문자열)에 있으면 True
    print("3이 리스트 안에 있습니다.")
if 3 not in data:   # 3이 리스트(문자열)에 없으면 True
    print("3이 리스트 안에 없습니다.")

## 5-2. pass문
##      : 조건이 True라고 해도, 아무것도 처리하고 싶지 않을 때 사용
score = 85
if score >= 80:
    pass
else:
    print("성적이 80점 미만입니다.")

print("프로그램을 종료합니다.")

## 5-3. 줄 바꿈 없이 간략하게 표현
score = 85
if score >= 80: result = "Success"
else: result = "Fail"
print(result)

## 5-4. 조건부 표현식
### 5-4-1. if ~ else문을 한 줄에 표현
score = 85
result = "Success" if score >= 80 else "Fail"
print(result)

### 5-4-2. 리스트에서 특정한 원소의 값 제거하기
### 1) 조건문의 형태로 구현
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

result = []

for i in a:
    if i not in remove_set:
        result.append(i)
print(result)

### 2) 조건부 표현식으로 구현
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

result = [i for i in a if i not in remove_set]
print(result)

# 6. 부등식
## 6-1. 파이썬에서는 수학의 부등식을 그대로 사용할 수 있다
x = 5
if 0 < x < 15:
    print("x는 0보다 크고 20보다 작은 수입니다.")