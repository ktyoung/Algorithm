# 반복문 #
# 1. while문
i = 1
result = 0

while i <= 9:       # i가 9보다 작거나 같을 때 아래 코드를 반복적으로 실행
    if i % 2 == 1:  # 홀수만 더하기
        result += i
    i += 1

print(result)

# 2. for문
# for 변수 in 리스트/튜플/문자열 등:
#     실행할 소스코드

result = 0
for i in range(1, 10):  # range(시작 값, 끝 값 + 1)
                        # 1부터 9까지의 수 저장
    result += i

print(result)

## 2-1. range()
##      : range()의 값으로 하나만 넣으면 시작값은 0이 됨
##      : 주로 리스트나 튜플 데이터의 모든 원소를 첫 번째 인덱스부터 방문할 때 사용
scores = [90, 85, 77, 65, 97]
for i in range(5):
    if scores[i] >= 80:
        print(i + 1, "번 학생은 합격입니다.")

## 2-2. continue
scores = [90, 85, 77, 65, 97]
cheating_list = {2, 4}
for i in range(5):
    if scores[i] in cheating_list:  # 블랙리스트에 등록된 번호는 무시하고 다음 번호부터 처리
        continue
    if scores[i] >= 80:
        print(i + 1, "번 학생은 합격입니다.")

## 2-3. 중첩 for문
for i in range(2, 10):
    for j in range(2, 10):
        print(i, " X ", j, " = ", i * j)
    print()        