# 함수 #

# 1. 함수 선언
# def 함수명(매개변수):
#     실행할 소스코드
#     return 반환 값

def add(x, y):
    print("두 수의 합은", x + y)
add(1, 2)
add(y = 7, x = 3)   # 인자의 값을 각각 전달

# 2. global 키워드
#    : 함수 안에서 함수 밖의 변수를 수정할 때 사용
a = 0

def func():
    global a    # a라는 지역 변수를 생성하지 않고, 함수 바깥에 선언된 a 변수를 참조
    a += 1

for i in range(10):
    func()

print(a)

# 3. 람다 표현식
print((lambda x, y: x + y)(3, 7))