import sys

# 입출력 #

# 1. 입력
#    : input() → 한 줄의 문자열을 입력받도록 함

## 1-1. 문자열을 띄어쓰기로 구분하여 정수형의 데이터로 저장
##      : list(map(int, input().split())) → 사용 빈도가 매우 높음

## 1-2. 입력을 위한 전형적인 소스코드
n = int(input())                        # 데이터의 개수 입력
data = list(map(int, input().split()))  # 각 데이터를 공백으로 구분하여 입력

data.sort(reverse = True)
print(data)

## 1-3. 공백을 기준으로 구분하여 적은 수의 데이터 입력
n, m, k = list(map(int, input().split()))
print(n, m, k)

## 1-4. 입력의 개수가 많은 경우 → sys.stdin.readline() 함수 사용
##      : sys 라이브러리를 사용할 땐, 한 줄을 입력 받은 후 rstrip() 함수를 반드시 호출해야 함
##        → 엔터가 줄바꿈 기호로 입력되는데, 이 공백 문자를 제거하기 위함
data = sys.stdin.readline().rstrip()
print(data)

# 2. 출력
## 2-1. 변수 출력 예시
a = 1
b = 2
print(a)    # print()는 출력 후에 줄바꿈을 수행함
print(b)
print(a, b)

## 2-2. 문자열과 변수를 함께 출력하기
answer = 7
# print("정답은" + answer + "입니다.") → 문자열과 수를 더하면 오류 발생

print("정답은 "+ str(answer) +" 입니다.") # 해결방법 1. str()함수로 변수 데이터를 문자열로 변환
print("정답은", answer, "입니다.")        # 해결방법 2. 각 자료형을 콤마(,)를 기준으로 구분
print(f"정답은 {answer} 입니다.")         # 해결방법 3. f-string
                                        #           : 문자열 앞에 'f'를 붙임으로써 사용... 중괄호{} 안에 변수 입력 가능