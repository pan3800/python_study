try:
    userData = int(input())
    result = int(10 / userData)
    print('result : {0}'.format(result))
except ZeroDivisionError as e:
    print('ZeroDivisionError 예외 발생 : {0}'.format(e))
except Exception as e:
    print('Exception 예외 발생 : {0}'.format(e))
