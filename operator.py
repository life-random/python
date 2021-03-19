a = 3; b = ~a; # ~은 뒤의 수의 1의 보수를 구함
print(a, b ,"b = b + 1 =>",(b+1))
# 같은 줄에 명령이 2개가 존재할 때 끝에 ;두어 구분한다.

a = 3; b = 5; c = a & b;
# AND 둘 중에 하나라도 0일면 0(둘 다 1이면 1)
print(a, b, c)

a = 3; b = 5; c = a ^ b;
print(a, b, c)
# exclusive OR 두 개가 같으면 0 다르면 1

a = 3; b = 5; c = a | b;
# OR 두 개 중에 하나라도 1이라면 1(둘 다 0이면 0)
print(a, b, c)
