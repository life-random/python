'''
hap = 0
i = 1
while i <= 100:
    hap += i
    i += 1

print("합 = %d" % hap)
'''
'''
evenHap = 0
oddHap = 0
i = 1
while i <= 100:
    if i % 2 ==0 :
        evenHap += i
    else:
        oddHap += i
    i += 1

print("짝수 합 = %d" % evenHap)
print("홀수 합 = %d" % oddHap)
'''
'''
sevenHap = 0
i = 1
while i <= 100:
    if i % 7 ==0:
        sevenHap += i

print("1-100 7의 배수의 합 = %d" % sevenHap)
'''
'''
Hap = 0
i = 1
while i <=100:
    Hap += i
    if Hap >= 1000:
        break
    i += 1
print("1-100 합 중에 처음으로 1000을 넘는 수 %d와 합 = %d" % (i, Hap))
'''
hap = 0
i = 0
while i <=100:
    i += 1
    if (i % 7 == 0):
        continue
    hap += i

print("1-100 합 중에 7의 배수는 생략한 합= %d" % hap)










































