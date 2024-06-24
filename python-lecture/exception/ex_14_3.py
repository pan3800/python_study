# 예외가 발생하지 않으면 else문 실행.
# 예외 발생 여부와 상관없이 항상 finally문 실행.

try:
    userData = int(input())
    result = int(10 / userData)
except:
    print('sorry~~')
else:
    print('예외가 발생하지 않았어요.')
finally:
    print('항상 실행 합니다.')



