marks = []

for i in range(5):
    scr = int(input("%d번의 학생의 점수 : " % (i+1)))
    marks.append(scr)
    

print(marks)
sum = 0
number = 0

for mark in marks:
    number += 1
    sum += mark
    if mark >=60:
        print("%d번 학생의 점수는 %d이고 합격입니다." % (number,mark))
    else:
        print("%d번 학생의 점수는 %d이고 불합격입니다." % (number, mark))

print("전체 총합은 %d이고 평균은 %d입니다" %(sum, (sum/number)))
