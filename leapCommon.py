year = int(input("연도를 입력하시오 : "))
#연산자 우선순위에 따라 산술, 관계, 논리연산 순으로 연산
#논리 연산은 not, and, or 순으로 연산

if(year%4 ==0 and year%100 !=0 or year%400 == 0):
    print("이번 년도는 윤년(leap year)입니다")
else:
    print("이번 년도는 평년(common year)입니다")
