# 파일 생성 방법
# 파이썬은 파일을 읽고 쓰기 위한 함수로 open(), write(), read(), close() 함수를 제공한다.
# f = open('/Users/imchaeseong/Documents/python/python_study/python-lecture/Input-output/textFile.txt', 'w')
# f.write('hello python')
# f.close()

# 파일 읽기 방법
f = open('/Users/imchaeseong/Documents/python/python_study/python-lecture/Input-output/textFile.txt', 'r')
print('f.read() : {0}'.format(f.read()))
f.close()


