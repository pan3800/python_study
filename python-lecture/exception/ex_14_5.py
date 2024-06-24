# 사용자가 Exception 클래스를 상속받아 예외 클래스를 만들 수 있다.

class MyException(Exception):
    def __init__(self, e):
        super().__init__('{0}으로 나눌수 없습니다.'.format(e))


def division(x, y):
    if y != 0:
        return x /y
    else:
        raise MyException(y)


try:
    numX = int(input())
    numY = int(input())
    result = division(numX, numY)
    print('result : {0}'.format(result))
except MyException as e:
    print('예외 발생 : {0}'.format(e))
else:
    print('정상 실행')
finally:
    print('자원 해제')
