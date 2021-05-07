# 사각형의 밑변과 높이을 입력받아 면적을 리턴하는 함수를 정의하고
# 테스트하는 프로그램을 작성하세요
# 단 사각형의 밑변과 높이는 사용자로부터 입력 받으세요!!
def calcArea(b, h):
    area = 3.14159 * b * h
    return area

radius = int(input("원의 반지름 : "))
radius = int(input("원의 반지름 : "))
print("반지름이", radius,"인 원의 면적은", area,"입니다.")
