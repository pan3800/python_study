# try - except
# 예외처리 없음
# userData = int(input())
# result = int(10 / userData)
# print('result : {0}'.format(result))


# 예외처리 있음
try:
        userData = int(input())
        result = int(10 / userData)
        print('result : {0}'.format(result))
except:
        print('sorry~~')