# 조건문 if 사용
num1 = 20
num2 = 30

# False
if num1 > num2:
    print('{0} > {1}'.format(num1, num2))
else:
    print('{0} <= {1}'.format(num1, num2))

# if ~ elif 사용법
score = 70

if score >= 90:
    print('수')
elif score >= 80:
    print('우')
elif score >= 70:
    print('양')
else:
    print('가')

