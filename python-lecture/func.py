# 매개 변수가 없을때
def myFun():
    print("Hello python")
    return

myFun()

# 매개 변수가 있을때
def myFun(str):
    print(str)
    return

myFun("Hello python")
myFun("Hello java")
myFun("Hello C++")
myFun("Hello world")
myFun(123)

# 매개 변수가 여러개 있을때
def myFun1(str1, str2):
    print(str1 + ' ' + str2)
    return

myFun1("Hello", "python")

def outputFun(str1, str2, str3, str4):
    print('{0} {1} {2} {3}'.format(str1, str2, str3, str4))
    return

outputFun('i', 'am', 'python', 'developer')

# 함수 return 반환
def calFun(x, y):
    result = x * y
    return result

calcurator = calFun(10, 20)
print(calcurator)

# 지역 변수와 전역 변수
result = 10
print('result : {0}'.format(result))

def fun(x, y):
    result1 = x + y
    print('result : {0}'.format(result1))

    return result1

print('fun_result : {0}'.format(fun(10, 100)))
print('result : {0}'.format(result))

